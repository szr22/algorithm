def maxReach(arr):
    maxReachPos = 0
    for i, num in enumerate(arr):
        if maxReachPos < i:
            return False
        maxReachPos = max(maxReachPos, num+i)
        if maxReachPos >= len(arr):
            return True
    return False
        


arr = [1, 0, 8, 8, 4, 2, 0, 0, 2, 1, 0]
res = maxReach(arr)
print(res)
