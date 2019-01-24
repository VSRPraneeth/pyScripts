import heapq

grades = [32, 45, 56, 66, 532, 45]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 564},
    {'ticker': 'FB', 'price': 64},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'YHOO', 'price': 58}
]

print(heapq.nsmallest(2, stocks, key= lambda stock: stock['price']))
