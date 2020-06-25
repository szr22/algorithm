#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
from collections import defaultdict
# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        res = ""
        self.pos = 0
        m = self.parse(formula)
        # print(m)
        for k in sorted(m.keys()):
            if m[k] == 1:
                res += k
            else:
                res += k + str(m[k])
        return res

    def parse(self, formula):
        res = defaultdict(int)
        while self.pos<len(formula):
            if formula[self.pos]=="(":
                self.pos += 1
                for k, v in self.parse(formula).items():
                    res[k] += v

            elif formula[self.pos]==")":
                self.pos += 1
                i = self.pos
                while self.pos<len(formula) and formula[self.pos].isdigit():
                    self.pos += 1
                multiStr = formula[i:self.pos]
                multi = 1
                if multiStr:
                    multi = int(multiStr)
                for k, v in res.items():
                    res[k] *= multi
                return res
            else:
                i = self.pos
                self.pos += 1
                while self.pos < len(formula) and formula[self.pos].islower():
                    self.pos += 1
                ele = formula[i:self.pos]

                i = self.pos
                while self.pos < len(formula) and formula[self.pos].isdigit():
                    self.pos += 1
                multiStr = formula[i:self.pos]
                multi = 1
                if multiStr:
                    res[ele] += int(multiStr)
                else:
                    res[ele] += multi
            # print(res)
        return res
# @lc code=end
formula = "Mg(OH)2"
formula = "K4(ON(SO3)2)2"
res = Solution().countOfAtoms(formula)
print(res)