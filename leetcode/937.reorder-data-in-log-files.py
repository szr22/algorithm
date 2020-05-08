#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

from typing import List
import re

# @lc code=start

class File(object):
    def __init__(self, name, content):
        self.content = content
        self.name = name

    def __gt__(self, other):
        if self.content > other.content:
            return True
        elif self.content < other.content:
            return False
        else:
            return self.name + self.content > other.name + other.content


    def __str__(self):
        return self.name + self.content

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_files = []
        dig_files = []

        for log in logs:
            l_name = log.split(' ')[0]
            l_cont = log[len(l_name):]
            print(l_cont)
            if re.match("^[0-9 ]+$", l_cont):
                dig_files.append(File(l_name, l_cont))
            else:
                let_files.append(File(l_name, l_cont))
        let_files.sort()
        res = []
        for f in let_files:
            res.append(str(f))
        for f in dig_files:
            res.append(str(f))
        return res

    def reorderLogFilesBetter(self, logs: List[str]) -> List[str]:
        d_logs = []
        l_logs = []
        res = []

        for log in logs:
            splited_log = log.split()
            if splited_log[1].isdigit():
                d_logs.append(log)
            else:
                l_logs.append([splited_log[0], ' '.join(splited_log[1:])])

        for item in sorted(l_logs, key=operator.itemgetter(1,0)):
            res.append(' '.join(item))
        return res + d_logs
# @lc code=end


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

res = Solution().reorderLogFiles(logs)
print(res)