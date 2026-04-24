import json
tickers = ['ADBE', 'AMZN', 'APPL', 'CSCO', 'GOOG', 'JPM', 'MSFT', 'QQQ', 'TSLA', 'VOO']
# function for mean reversion strategy
def meanReversionStrategy(prices, ticker):
    print(ticker, "Mean Reversion Strategy Output:")
# setting up variables to track buy price, first buy price, and total profit
    buy_price = 0
    first_buy = 0
    total_profit = 0
# loop through prices starting from the 5th price to calculate the average of the previous 5 prices
    for i in range(5, len(prices)):
        avg = sum(prices[i-5:i]) / 5
        price = prices[i]

        if price < avg * 0.98 and buy_price == 0:
            buy_price = price

            if first_buy == 0:
                first_buy = price

            print("buying at:      ", price)

        elif price > avg * 1.02 and buy_price != 0:
            profit = price - buy_price
            total_profit += profit

            print("selling at:     ", price)
            print("trade profit:   ", round(profit, 2))

            buy_price = 0

    percent_return = 0
    if first_buy != 0:
        percent_return = (total_profit / first_buy) * 100
# print the results for total profit, first buy price, and percent return, making it look nice and clean
    print("-----------------------")
    print("Total profit:   ", round(total_profit, 2))
    print("First buy:      ", first_buy)
    print("Percent return: ", round(percent_return, 2), "%")
    print()

    return round(total_profit, 2), round(percent_return, 2)

# same thing but for the simple moving average strategy, just with different buy/sell conditions
def simpleMovingAverageStrategy(prices, ticker):
    print(ticker, "Simple Moving Average Strategy Output:")

    buy_price = 0
    first_buy = 0
    total_profit = 0

    for i in range(5, len(prices)):
        avg = sum(prices[i-5:i]) / 5
        price = prices[i]

        if price > avg and buy_price == 0:
            buy_price = price

            if first_buy == 0:
                first_buy = price

            print("buying at:      ", price)

        elif price < avg and buy_price != 0:
            profit = price - buy_price
            total_profit += profit

            print("selling at:     ", price)
            print("trade profit:   ", round(profit, 2))

            buy_price = 0

    percent_return = 0
    if first_buy != 0:
        percent_return = (total_profit / first_buy) * 100

    print("-----------------------")
    print("Total profit:   ", round(total_profit, 2))
    print("First buy:      ", first_buy)
    print("Percent return: ", round(percent_return, 2))
    print()

    return round(total_profit, 2), round(percent_return, 2)

# function to save results to a json file
def saveResults(results):
    json_results = 'Homework5/results.json'
    with open(json_results, "w") as file:
        json.dump(results, file, indent=4)

#creating my tickers list and results dictionary to store the prices, profits, and returns for each ticker and strategy
tickers = ['ADBE', 'AMZN', 'APPL', 'CSCO', 'GOOG', 'JPM', 'MSFT', 'QQQ', 'TSLA', 'VOO']
results = {"prices": [], "profits": [], "returns": []}

# loop through each ticker, read the prices from the corresponding text file, and run both strategies to calculate profits and returns, storing everything in the results dictionary
for ticker in tickers:
    with open('/workspaces/data_3500_homework/Homework5/' + ticker + '.txt') as f:
        next(f) # skip the first line of the file which contains the header --- IGNORE ---
        prices = [float(line.split()[1]) for line in f if line.strip()]

    results[ticker + "_prices"] = prices
# run the simple moving average strategy and store the profit and return in the results dictionary
    sma_profit, sma_return = simpleMovingAverageStrategy(prices, ticker)
    results[ticker + "_sma_profit"] = sma_profit
    results[ticker + "_sma_returns"] = sma_return
# run the mean reversion strategy and store the profit and return in the results dictionary
    mr_profit, mr_return = meanReversionStrategy(prices, ticker)
    results[ticker + "_mr_profit"] = mr_profit
    results[ticker + "_mr_returns"] = mr_return
# save the results to a json file by calling the saveResults function
saveResults(results)
print("Results have been saved")
