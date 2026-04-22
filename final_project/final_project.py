#import libraries
import requests
import pandas as pd
import json

# file name
csv_file = "final_project/treasury_data.csv"
json_file = "final_project/results.json"

# api setup, the rest of the perameters are established in the code because I have to check and change the date
base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
# This endpoint retrieves daily Treasury operating cash data, including deposits and withdrawals, which shows how much money is entering and leaving the Treasury each day.
endpoint = "/v1/accounting/dts/deposits_withdrawals_operating_cash"


# test to see if the csv file already exists and is up to date
try:
    df = pd.read_csv(csv_file)
    df["record_date"] = pd.to_datetime(df["record_date"])
    # make sure that the transaction amounts are numeric, if there are any non-numeric values they will be set to NaN and then we will drop those rows since we can't use them for analysis because the NaN values will mess that up. 
    df["transaction_today_amt"] = pd.to_numeric(df["transaction_today_amt"], errors="coerce")

    # find most recent date already saved in the csv, we use normalize to set the time to 00:00:00 so that we can compare it to yesterday's date which is also normalized, this way we are just comparing the dates without worrying about the time of day, we will normalize all of the dates in the rest of the code. 
    latest_date = df["record_date"].max().normalize()

    # get today's date, the api updates daily at the end of the day so we check the day before
    yesterday = pd.Timestamp.today().normalize() - pd.Timedelta(days=1)

   #if the date is already up to date, skip the API pull and move on to the analysis
    if latest_date >= yesterday:
        print("Records are already up to date.")
        print("No API pull needed.")

   # if the API is not up to date, pull new data and update the csv
    else:
        print("Trying to pull new data from API (this might take a moment)...")

        params = {
            "fields": "record_date,transaction_type,transaction_catg,transaction_today_amt",
            "filter": f"record_date:gt:{latest_date.date()}",
            "sort": "-record_date",
            "format": "json",
            "page[size]": 1000
        }
# the API has a default page size of 100, so we need to loop through pages until we get all the new data, I used AI to help me with this code because I didn't really know all the correct syntax 
        all_data = []
        page = 1

        while True:
            params["page[number]"] = page
            response = requests.get(f"{base_url}{endpoint}", params=params)

            if response.status_code != 200:
                print('No more data to pull or error occurred. Status code:', response.status_code)
                break

            data = response.json()
            rows = data["data"]

            if not rows:
                break

            all_data.extend(rows)
            print(f"Pulled page {page} with {len(rows)} rows")
            page += 1

        if all_data:
            new_df = pd.DataFrame(all_data)

            # clean new data, make sure that the dates are in the correct format and that the amounts are numeric, then drop any rows with missing values since we can't use those for analysis
            new_df["record_date"] = pd.to_datetime(new_df["record_date"])
            new_df["transaction_today_amt"] = pd.to_numeric(new_df["transaction_today_amt"], errors="coerce")
            new_df = new_df.dropna()

            # combine old + new data using concat, concat means that we are just stacking the new rows on top of the old rows. 
            combined_df = pd.concat([df, new_df], ignore_index=True)

            # remove duplicates if they exist (shouldn't be any, but just in case)
            combined_df = combined_df.drop_duplicates(
                subset=["record_date", "transaction_type", "transaction_catg", "transaction_today_amt"]
            )
            df = combined_df

            # sort by date in descending order
            df = df.sort_values(by="record_date", ascending=False)

            # save updated csv to the original file, we set index to false because we don't need the old index numbers from the original csv and we want to create new ones for the combined data
            df.to_csv(csv_file, index=False)

            print("CSV updated successfully.")

        else:
            print("No new rows were returned from the API.")

# if the file doesn't exist, we need to pull all the data from the API and create the csv for the first time
except FileNotFoundError:
    print("CSV not found. Creating new file from API...")

    params = {
        "fields": "record_date,transaction_type,transaction_catg,transaction_today_amt",
        "filter": "record_date:gte:2024-01-01",
        "sort": "-record_date",
        "format": "json",
        "page[size]": 1000
    }
# the API has a default page size of 100, so we need to loop through pages until we get all the new data, I used AI to help me with this code because I didn't really know all the correct syntax 
    all_data = []
    page = 1

    while True:
        params["page[number]"] = page
        response = requests.get(f"{base_url}{endpoint}", params=params)

        if response.status_code != 200:
            print('No more data to pull or error occurred. Status code:', response.status_code)
            break

        data = response.json()
        rows = data["data"]

        if not rows:
            break

        all_data.extend(rows)
        print(f"Pulled page {page} with {len(rows)} rows")
        page += 1
# this is kindof a repeat from above so read the above comments
    df = pd.DataFrame(all_data)

    # clean data
    df["record_date"] = pd.to_datetime(df["record_date"])
    df["transaction_today_amt"] = pd.to_numeric(df["transaction_today_amt"], errors="coerce")
    df = df.dropna()

    # sort by date
    df = df.sort_values(by="record_date", ascending=False)

    # save first csv
    df.to_csv(csv_file, index=False)

    print("CSV created successfully.")
    print("Total rows:", len(df))


# start of the analysis, AI was used to help me decide what analysis to perform and to help me write the code for the analysis. 
'''
This analysis examines daily U.S. Treasury cash activity by looking at deposits and withdrawals over time. It first summarizes the dataset by showing the number of records and the date range covered. It then calculates the average transaction amount to understand the typical size of cash movements. The analysis also compares total deposits and withdrawals to determine whether more money is entering or leaving the Treasury overall. Finally, it groups transactions by date to show how activity changes over time, helping identify patterns or spikes in cash flow. Overall, this analysis provides insight into short-term Treasury cash trends and whether there are net inflows or outflows.
'''

    # Basic info for analysis 
results = {}
results["summary"] = {
    "total_rows": int(len(df)),
    "start_date": str(df["record_date"].min().date()),
    "end_date": str(df["record_date"].max().date())
}

# Average transaction amount
results["average_amount"] = float(df["transaction_today_amt"].mean())

# group by the total deposits vs withdrawals
totals = df.groupby("transaction_type")["transaction_today_amt"].sum().reset_index()
results["totals_by_type"] = totals.to_dict(orient="records")

# One simple trend (daily total)
daily = df.groupby("record_date")["transaction_today_amt"].sum().reset_index()
daily["record_date"] = daily["record_date"].dt.strftime("%Y-%m-%d")
results["daily_totals"] = daily.to_dict(orient="records")

# save results to json file
with open(json_file, "w") as f:
    json.dump(results, f, indent=4)
print("results.json created/updated")