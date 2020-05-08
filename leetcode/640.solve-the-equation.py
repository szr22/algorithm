#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        leftS = 0
        rightS = 0
        lastEnd = 0
        dirc = 1
        for i in range(len(equation)):
            if equation[i] in '+-=':
                if i==0 or equation[i-1]=='=':
                    continue
                if equation[i-1]=='x':
                    numStr = equation[lastEnd:i-1]

                    if numStr in '+-':
                        numStr += '1'
                    leftS += int(numStr)*dirc
                else:
                    numStr = (equation[lastEnd:i])
                    rightS -= int(numStr)*dirc
                    # print(rightS)
                lastEnd = i
                if equation[i]=='=':
                    dirc *= -1
                    lastEnd=i+1
        if equation[-1] == 'x':
            numStr = equation[lastEnd:-1]
            if numStr in '+-' or not numStr:
                numStr += '1'
            leftS += int(numStr)*dirc
        else:
            numStr = (equation[lastEnd:])
            rightS -= int(numStr)*dirc

        # print(leftS, rightS)
        if leftS == 0:
            if rightS == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        return 'x='+str(rightS//leftS)



# @lc code=end

equation = "-x+5-3+x=-6+x-2"
equation = 'x=x'
res = Solution().solveEquation(equation)
print(res)