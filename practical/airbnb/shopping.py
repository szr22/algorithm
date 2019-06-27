import collections
from decimal import Decimal

menu = {
    'friut': 2.64,
    'fries': 2.00,
    'pasta': 1.32,
    'bee': 1.00
}

res = set()

def shopping(amount, cur):
    if 0<amount<min(menu.values()) or amount<0:
        return
    if amount == 0:
        cur.sort()
        res.add(','.join(cur))
        return
    for k, v in menu.items():
        shopping(round(amount-v, 2), cur+[k])

shopping(6.64, [])

print(res)