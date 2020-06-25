#
# @lc app=leetcode id=736 lang=python3
#
# [736] Parse Lisp Expression
#
from collections import defaultdict
# @lc code=start
class Solution:
    def evaluate(self, expression: str) -> int:
        def isNum(s):
            try:
                int(s)
                return True
            except:
                return False

        def find(start, needNum=True):
            if expression[start] == "(":
                return helper(start+1)
            else:
                i = start
                while expression[i] not in " )":
                    i += 1
                res = expression[start:i]
                if isNum(res):
                    return int(res), i-1
                else:
                    if needNum:
                        return values[res], i-1
                    return res, i-1

        def helper(start):
            i = start
            while expression[i] != " ":
                i += 1
            op = expression[start:i]
            if op == "let":
                return let(i+1)
            else:
                return compute(i+1, op)

        def compute(start, op):
            x, i = find(start)
            y, j = find(i+2)
            if op=="add":
                return x+y, j+1
            return x*y, j+1

        def let(start):
            changed = {}
            while True:
                x, i = find(start, False)
                if expression[i+1] == ")":
                    tmp = (values[x] if x in values else x, i+1)
                    for x in changed:
                        if changed[x] != None:
                            values[x] = changed[x]
                        else:
                            del values[x]
                    return tmp
                y, j = find(i+2)
                changed[x] = values[x] if x in values else None
                values[x] = y
                start = j+2

        values = {}
        return helper(1)[0]

# @lc code=end
exp = "(add 1 2)"
exp = "(let a1 3 b2 (add a1 1) b2)"
res = Solution().evaluate(exp)
print(res)