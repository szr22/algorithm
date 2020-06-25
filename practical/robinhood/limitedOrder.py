from collections import defaultdict
import bisect

orders = [
    ["AAPL", "S", "119"],
    ["AAPL", "S", "120"],
    ["AAPL", "B", "117"],
    ["AAPL", "B", "116"],
    ["AAPL", "B", "115"],
]

poolSale = defaultdict(list)
poolBuy = defaultdict(list)

for ticker, op, price in orders:
    if op == "B":
        pos = bisect.bisect_right(poolSale[ticker], price)
        if pos<len(poolSale[ticker]):
            poolSale[ticker].pop()
        else:
            bisect.insort(poolBuy[ticker], price)
    if op == "S":
        pos = bisect.bisect_left(poolBuy[ticker], price)
        if pos>0:
            poolBuy[ticker].pop(pos-1)
        else:
            bisect.insort(poolSale[ticker], price)
    print(poolBuy)
    print(poolSale)