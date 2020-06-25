#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueueExtraSpace(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for i, j in people:
            res.insert(j,[i,j])
        return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        for i in range(len(people)):
            cnt = 0
            for j in range(i):
                if cnt == people[i][1]:
                    t = people[i]
                    for k in range(i-1, j-1, -1):
                        people[k+1] = people[k]
                    people[j] = t
                    break
                cnt += 1
        return people
# @lc code=end

