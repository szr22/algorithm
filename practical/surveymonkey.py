def getLongestIncSub(numArr):
    if not numArr:
        return []

    if len(numArr)==1:
        return numArr

    res = [numArr[0]]

    for i in range(1, len(numArr)):
        tmp = getLongestIncSub(numArr[i:])
        print(res)
        if tmp and tmp[0]>res[-1]:
            res += tmp

        if len(tmp)>=len(res):
            res = tmp

    return res

def lengthOfLIS(nums) -> int:
    n = len(nums)
    res = []
    dp = [[nums[i]] for i in range(n)]

    res = []
    for i in range(1, n):
        for j in range(i):
            if nums[i]>nums[j]:
                if len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[j]+[nums[i]]

        if len(dp[i])>len(res):
            res = dp[i]
    return res

numArr = [12, 5, 6, 7, 6]
res = getLongestIncSub(numArr)
print(res)