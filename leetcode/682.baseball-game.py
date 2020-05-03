#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                if stack:
                    stack.pop()
            elif op == 'D':
                stack.append(stack[-1]*2)
            elif op == '+':
                if len(stack)>=2:
                    stack.append(
                        stack[-1]+stack[-2]
                    )
            else:
                stack.append(int(op))
        return sum(stack)

# @lc code=end

