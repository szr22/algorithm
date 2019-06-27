import sys
import random

def max_sub_arr(arr):
    res = -sys.maxsize
    cur = -sys.maxsize
    for num in arr:
        cur = max(cur+num, num)
        res = max(res, cur)
        print(cur, res)
    return res

if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-10,10))
    print(arr)
    # arr = [6, -9, 9, -9, 3, -10, -1, -10, 5, 2]
    res = max_sub_arr(arr)
    print(res)