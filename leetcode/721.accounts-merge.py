#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        hashMap = defaultdict(list)
        n = len(accounts)
        visited = [False]*n
        for idx, acct in enumerate(accounts):
            for i in range(1, len(acct)):
                hashMap[acct[i]].append(idx)
        for i in range(n):
            if visited[i]:
                continue
            queue = [i]
            emailSet = set()
            while queue:
                idx = queue.pop(0)
                visited[idx] = True
                emails = accounts[idx][1:]
                for email in emails:
                    emailSet.add(email)
                    for ownerIdx in hashMap[email]:
                        if visited[ownerIdx]:
                            continue
                        queue.append(ownerIdx)
                        visited[ownerIdx] = True

            res.append([accounts[i][0]]+sorted(emailSet))
        return sorted(res, key=lambda r:res[0])

    def accountsMergeBad(self, accounts: List[List[str]]) -> List[List[str]]:
        ownerMap = defaultdict(str)
        emialMap = defaultdict(str)
        rootHashmap = defaultdict(set)
        res = []
        for _, account in enumerate(accounts):
            for i in range(1, len(account)):
                ownerMap[account[i]] = account[0]
                emialMap[account[i]] = account[i]

        for _, account in enumerate(accounts):
            rootEmail = self.findRoot(account[1], emialMap)
            # update all realated email
            for i in range(2, len(account)):
                emialMap[self.findRoot(account[i], emialMap)] = rootEmail

        for _, account in enumerate(accounts):
            for i in range(1, len(account)):
                rootHashmap[self.findRoot(account[i], emialMap)].add(account[i])

        for rootEmail, emails in rootHashmap.items():
            res.append([ownerMap[rootEmail]]+sorted(emails))

        return sorted(res, key=lambda r:res[0])

    def findRoot(self, email, emialMap):
        return email if emialMap[email] == email else self.findRoot(emialMap[email], emialMap)

# @lc code=end

accounts = [
    ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]
]
res = Solution().accountsMerge(accounts)
# print(res)

accounts = [
    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
]
res = Solution().accountsMerge(accounts)
print(res)