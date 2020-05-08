#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        cntList = list(cnt.items())
        cntList.sort(key=lambda x: x[1], reverse=True)
        mxCnt = cntList[0][1]
        taskLen = len(tasks)
        mostComCnt=0
        for item in cntList:
            if item[1] == mxCnt:
                mostComCnt+=1
            else:
                break
        return max(taskLen, (mxCnt-1)*(n+1)+mostComCnt)
# @lc code=end

tasks = ["A","A","A","B","B","B"]
n = 2

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

res = Solution().leastInterval(tasks, n)
print(res)