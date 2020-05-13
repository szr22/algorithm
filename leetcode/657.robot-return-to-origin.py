#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def __init__(self):
        self.moveMap = {
            'L': [0, -1],
            'R': [0, 1],
            'U': [1, 0],
            'D': [-1, 0],
        }
        self.orginPos = [0, 0]

    def judgeCircleStraight(self, moves: str) -> bool:
        curPos = self.orginPos.copy()
        for c in moves:
            curPos[0] += self.moveMap[c][0]
            curPos[1] += self.moveMap[c][1]
            # print(curPos)
        return curPos == self.orginPos

    def judgeCircle(self, moves: str) -> bool:
        return (
            moves.count('R') == moves.count('L')
            and moves.count('U') ==moves.count('D')
        )

# @lc code=end

res = Solution().judgeCircle('LL')
print(res)
