# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        for i, num in enumerate(nums):
            max_pos = max(max_pos, num+i)
            if max_pos >= n-1:
                return True
            if max_pos < i+1:
                return False
        return False


nums = [3,0,8,2,0,0,1]
res = Solution().canJump(nums)
print(res)