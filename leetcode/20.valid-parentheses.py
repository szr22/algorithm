#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = {
            '(': 1,
            '[': 2,
            '{': 3,
        }
        right = {
            ')': 1,
            ']': 2,
            '}': 3,
        }
        stack = []
        for char in s:
            if char in left.keys():
                stack.append(char)
            else:
                if (
                    not stack
                    or left[stack.pop()] != right[char]
                ):
                    return False
        return len(stack) == 0

# @lc code=end

