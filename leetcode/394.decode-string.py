#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        cur_str = ''
        cur_num = 0
        stack = []
        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                pre_num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + pre_num*cur_str
            elif c.isdigit():
                cur_num = cur_num*10 + int(c)
            else:
                cur_str += c
        return cur_str


# @lc code=end

