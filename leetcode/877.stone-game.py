#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        left, right = 0, len(piles)-1
        alex, lee = 0, 0
        round=0
        while(left<=right):
            if round==0:
                if piles[left]<piles[right]:
                    alex+=piles[right]
                    right-=1
                else:
                    alex+=piles[left]
                    left+=1

            elif round==1:
                if piles[left]<piles[right]:
                    lee+=piles[left]
                    left+=1
                else:
                    lee+=piles[right]
                    right-=1
            round=(round+1)%2

        return True if alex>lee else False
# @lc code=end

