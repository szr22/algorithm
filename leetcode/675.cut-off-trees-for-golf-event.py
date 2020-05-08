#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#
from typing import List
# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        h = len(forest)
        w = len(forest[0])
        tree = []
        res = 0
        for y in range(h):
            for x in range(w):
                if forest[y][x]>0:
                    tree.append((forest[y][x], y, x))
        tree.sort()
        i = 0
        x, y = 0, 0
        while i<len(tree):
            cnt = self.helper(forest, y, x, tree[i][1], tree[i][2])
            if cnt == -1:
                return -1

            res += cnt
            y = tree[i][1]
            x = tree[i][2]
            i += 1
        return res

    def helper(self, forest, y, x, treeY, treeX):
        if y==treeY and x==treeX:
            return 0
        h = len(forest)
        w = len(forest[0])
        cnt = 0
        queue = [[y,x]]
        visted = [[0 for _ in range(w)] for _ in range(h)]
        direction = [-1, 0, 1, 0, -1]

        while queue:
            cnt += 1
            i = 0
            q_len = len(queue)
            while i<q_len:
                r = queue[0][0]
                c = queue[0][1]
                queue.pop(0)
                # print(r,c)
                for k in range(4):
                    a = r+direction[k]
                    b = c+direction[k+1]
                    if a<0 or a>=h or b<0 or b>=w or visted[a][b]==1 or forest[a][b]==0:
                        continue
                    if a==treeY and b==treeX:
                        return cnt
                    visted[a][b] = 1
                    queue.append([a,b])
                i += 1
        return -1



# @lc code=end

forest = [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
forest = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
res = Solution().cutOffTree(forest)
print(res)