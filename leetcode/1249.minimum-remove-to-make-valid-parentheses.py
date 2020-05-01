#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def __init__(self):
        self.left = '('
        self.right = ')'

    def minRemoveToMakeValid(self, s: str) -> str:
        stock = []
        # keep record of the remove list
        mark = []
        for i, c in enumerate(s):
            if c == ')':
                if stock:
                    stock.pop()
                else:
                    mark.append(i)
            if c == '(':
                stock.append(i)
        # add rest position to the remove list
        if stock:
            mark.extend(stock)
        mark.sort(reverse=True)

        # loop through from the back will not impact previous order
        for i in mark:
            s = s[:i]+s[i+1:]
        return s


# @lc code=end

s = "lee(t(c)o)de)"
s = "a)b(c)d"
s = "))(("
s = "(a(b(c)d)"

res = Solution().minRemoveToMakeValid(s)

print(res)