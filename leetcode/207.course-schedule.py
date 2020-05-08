#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for req in prerequisites:
            graph[req[1]].append(req[0])
            visited[req[0]] += 1
        queue = []
        for i in range(numCourses):
            if visited[i]==0:
                queue.append(i)

        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for suc in graph[pre]:
                visited[suc] -= 1
                if visited[suc]==0:
                    queue.append(suc)
        return len(res) == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0 for _ in range(numCourses)]
        for req in prerequisites:
            self.graph[req[1]].append(req[0])
        for i in range(numCourses):
            if self.dfs(i):
                return False
        return True

    def dfs(self, curIdx):
        if self.visited[curIdx] == 1:
            return True
        if self.visited[curIdx] == 2:
            return False
        self.visited[curIdx] = 1
        for suc in self.graph[curIdx]:
            if self.dfs(suc):
                return True
        self.visited[curIdx] = 2
        return False

# @lc code=end

