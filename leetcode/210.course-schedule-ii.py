#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import List
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for req in prerequisites:
            graph[req[1]].append(req[0])
            visited[req[0]] += 1

        queue = []
        for i in range(numCourses):
            # push no pre requerst course
            if visited[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for suc in graph[pre]:
                visited[suc] -= 1
                # all pre req has finished
                if visited[suc] == 0:
                    queue.append(suc)

        if len(res) != numCourses:
            return []
        else:
            return res


# @lc code=end

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

res = Solution().findOrder(numCourses, prerequisites)
print(res)