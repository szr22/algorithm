#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#

# @lc code=start
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        cnt = Counter(arr)
        for num in sorted(cnt, key = lambda x:abs(x)):
            if cnt[num * 2] >= cnt[num]:
                cnt[num * 2] -= cnt[num]
            else:
                return False
        return True
# @lc code=end

