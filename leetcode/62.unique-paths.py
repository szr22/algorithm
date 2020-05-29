#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(m)]
        for _ in range(1, n):
            cur = [1]
            for c in range(1, m):
                cur.append(cur[c-1]+row[c])
            row = cur
        return row[-1]
# @lc code=end

