#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def findNext(pre):
            curr = [0] * len(cells)
            curr[0] = 0
            for j in range(1, len(cells)-1):
                #print(pre[j-1], pre[j+1])
                if pre[j-1] != pre[j+1]:
                    curr[j] = 0
                else:
                    curr[j] = 1
            curr[len(cells)-1] = 0
            return curr

        cycle = []
        state = findNext(cells)
        while state not in cycle:
            cycle.append(state)
            state = findNext(state)

        return cycle[(N - 1)%len(cycle)]
# @lc code=end

