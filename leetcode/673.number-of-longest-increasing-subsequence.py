#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
from typing import List
# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        res = 0
        mx = 0
        n = len(nums)
        num_len = [1 for _ in range(n)]
        num_cnt = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i]<=nums[j]:
                    continue
                if num_len[i] == num_len[j]+1:
                    num_cnt[i] += num_cnt[j]
                elif num_len[i] < num_len[j]+1:
                    num_len[i] = num_len[j]+1
                    num_cnt[i] = num_cnt[j]
            if mx == num_len[i]:
                res += num_cnt[i]
            elif mx < num_len[i]:
                mx = num_len[i]
                res = num_cnt[i]
            # print(num_len)
            # print(num_cnt)
            # print()
        return res

# @lc code=end

nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
res = Solution().findNumberOfLIS(nums)
print(res)