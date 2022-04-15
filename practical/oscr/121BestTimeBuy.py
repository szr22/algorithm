import sys
def max_profit(prices):
    min_price = sys.maxsize
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price-min_price)
    return max_profit

prices = [7,6,4,3,1]
res = max_profit(prices)
print(res)


def max_profit2(prices):
    profit = 0
    if len(prices) < 2:
        return 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx-1]:
            profit += prices[idx]-prices[idx-1]
    return profit

prices = [7,1,5,3,6,4]
res = max_profit2(prices)
print(res)


def max_profit3(prices):
    buy1, buy2 = -sys.maxsize, -sys.maxsize
    sold1, sold2 = 0, 0
    for price in prices:
        sold2 = max(sold2, buy2 + price)
        buy2 = max(buy2, sold1 - price)
        sold1 = max(sold1, buy1 + price)
        buy1 = max(buy1, -price)
        print(sold2, buy2, sold1, buy1)
    return sold2

prices = [3,3,5,1,0,3,1,4]
res = max_profit3(prices)
print(res)