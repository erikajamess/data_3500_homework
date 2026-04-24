tickers = ['ADBE', 'AMZN', 'APPL', 'CSCO', 'GOOG', 'JPM', 'MSFT', 'QQQ', 'TSLA', 'VOO']
results = {"prices": [], "profits": [], "returns": []}

# loop through each ticker, read the prices from the corresponding text file, and run both strategies to calculate profits and returns, storing everything in the results dictionary
for ticker in tickers:
    with open('/workspaces/data_3500_homework/Homework5/' + ticker + '.txt') as f:
        
        prices = [float(line.split()[1]) for line in f if line.strip()]