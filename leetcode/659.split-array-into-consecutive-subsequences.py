#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

from collections import Counter, defaultdict
from typing import List
# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)
        need_map = defaultdict(int)
        for num in nums:
            # may used in prev check
            if freq_map[num]==0:
                continue
            if need_map[num]>0:
                need_map[num] -= 1
                need_map[num+1] += 1
            # not in need map check the following 2 nums
            elif freq_map[num+1]>0 and freq_map[num+2]>0:
                need_map[num+3] += 1
                freq_map[num+1] -= 1
                freq_map[num+2] -= 1
            else:
                return False

            freq_map[num] -= 1

        return True

# @lc code=end
