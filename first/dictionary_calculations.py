stocks = {
    'GOOG' : 434,
    'AAPL' : 325,
    'AMZN' : 434,
    'FB' : 54,
    'MSFT' : 128,
}


min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

