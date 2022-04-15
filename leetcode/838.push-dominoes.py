#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
from collections import deque

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ""

        buffer_count = 0

        is_falling_right = False

        for c in dominoes:
            if c == ".":
                buffer_count += 1

            elif c == 'L':
                if is_falling_right:
                    q, r = divmod(buffer_count + 1, 2)

                    result += "R" * q + ("" if r == 0 else ".") + "L" * q

                    buffer_count = 0
                    is_falling_right = False
                else:
                    result += "L" * (buffer_count + 1)
                    buffer_count = 0

            elif c == 'R':
                if is_falling_right:
                    result += 'R' * buffer_count
                    buffer_count = 1
                    is_falling_right = True
                else:
                    result += "." * buffer_count
                    buffer_count = 1
                    is_falling_right = True
            else:
                if buffer_count != 0:
                    if is_falling_right:
                        c = 'R'
                    else:
                        c = '.'
                    result += c * buffer_count

        return result


# @lc code=end

