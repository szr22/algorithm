#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxTotal = total
        # for i in range(k):
        #     total += nums[i]

        # maxTotal = total
        for i in range(k, len(nums)):
            total = total+nums[i]-nums[i-k]
            # maxTotal = max(total, maxTotal)
            if maxTotal<total:
                maxTotal=total
                
        return maxTotal/k
# @lc code=end

