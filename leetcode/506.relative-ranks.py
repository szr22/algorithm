#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
import heapq
# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = len(nums)
        cnt = 1
        res = ['' for _ in range(n)]
        arr = []
        for i in range(n):
            arr.append([nums[i], i])
        arr.sort()
        for i in range(n):
            idx = arr.pop()[1]
            if cnt == 1:
                res[idx] = 'Gold Medal'
            elif cnt == 2:
                res[idx] = 'Silver Medal'
            elif cnt == 3:
                res[idx] = 'Bronze Medal'
            else:
                res[idx] = str(cnt)
            cnt += 1
        return res
# @lc code=end

