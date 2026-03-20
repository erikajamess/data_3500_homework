with open('/workspaces/data_3500_homework/Homework4/TSLA.txt') as file:
    daily_prices = [float(line.strip()) for line in file.readlines()] #reads each line from the file, cleans it up, converts it to a number, and stores everything in a list.

print('TSLA Mean Reversion Strategy Output: 2025 - 2026 Data:')
print('------------------------------------------------------')

buy = 0 #store the buy price
profit = 0 #keep a running total of the profit. 
have_stock = False #keeps track of weather we own the stock
first_buy = None   # store first purchase price here

for i in range(len(daily_prices)): # loop through each position in the price list from i to the end of the list
    current_price = daily_prices[i] # sets the current price ot the daily price at the current index 
    if i >= 5: #starts at index five then will move down with i-1, i-2 ect. adss them all together and then divides them to create an average. 
        moving_avg = (daily_prices[i-1] + daily_prices[i-2] + daily_prices[i-3] + daily_prices[i-4] + daily_prices[i-5]) / 5
        moving_avg = round(moving_avg, 2) # rounds it to two decimal places 

        if current_price < moving_avg * 0.98 and have_stock == False: #check to make sure we need to buy
            buy = current_price
            have_stock = True
            if first_buy is None:
                first_buy = buy #this allows us to store the first buy price 
            print("Buy at: $", buy)

        elif current_price > moving_avg * 1.02 and have_stock == True: #check to see if we should sell 
            sell = current_price
            trade_profit = sell - buy
            profit += trade_profit #adds to the running total
            have_stock = False #we no longer have the stock so we need to sell 

            print("Sell at: $", sell, "Profit on the sale: $", round(trade_profit, 2))

        else:
            pass
print('------------------------------------------------------')
# calculate final profit % and print out our other calculations
if first_buy is not None: #makes sure that we have bought stock, this allow us to calculate everything. 
    final_profit_percentage = (profit / first_buy) * 100
    print("Total Profit: $", round(profit, 2))
    print("First Buy: $", first_buy)
    print("Return (%):", round(final_profit_percentage, 2),'%')
else:
    print("No trades executed.")
print('------------------------------------------------------')