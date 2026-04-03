# define function meanReversionStrategy
import json
def meanreversionstrategy():
    #run strategy and output buys/sells, final profit, and final percentage returns
    #return profit and returns
    pass
def simpleMovingAverageStrategy():
    #run strategy and output buys/sells, final profit, and final percentage returns
    #return profit and returns
    pass
def saveResults(results):
    json.dump(results, 'open()/workspaces/data_3500_homework/Homework5/results.json','w',indent=1)
# define function simpleMovingAverageStrategy

#    run strategy and output buys/sells, final profit, and final percentage returns

#    return profit and returns


# define function saveResults


# create list to store 10 tickers

# create dictionary called results to store prices, profits and return percentages


# loop through the list of tickers

for ticker in tickers:

# load prices from a file <ticker>.txt, and store them in the results dictionary with the key “<ticker>_prices”

# call meanReversionStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_mr_profit” and “<ticker>_mr_returns”

# call simpleMovingAverageStrategy(prices) and store the profit and returns in the results dictionary with the keys “<ticker>_sma_profit” and “<ticker>_sma_profit”

saveResults(results) # do this last and outside of for loop - save the results dictionary to a file called results.json
 

# Here is the logic for the simple moving average strategy and the mean reversion strategy:

# # mean reversion average trading strategy logic

# if price < avg * .98:
#    print("buy at: ", price)
# elif price > avg * 1.02:
#    print("sell at: ", price)
# else:
#    pass

# # simple moving average trading strategy logic

# if price > avg:
#    print("buy at: ", price)
# elif price < avg:
#    print("sell at: ", price)
# else:
#     pass
