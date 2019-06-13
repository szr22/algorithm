from typing import List
class Solution:
    def wordsAbbreviation(self, wordDict: List[str]) -> List[str]:
        n = len(wordDict)
        res = [0 for _ in range(n)]
        pre = [1 for _ in range(n)]
        for i in range(n):
            res[i] = self.abbreviate(wordDict[i], pre[i])
        for i in range(n):
            while True:
                s = set()
                for j in range(i+1, n):
                    if res[j] == res[i]:
                        s.add(j)
                if not s:
                    break
                s.add(i)
                for a in s:
                    pre[a] += 1
                    res[a] = self.abbreviate(wordDict[a], pre[a])
        return res

    def abbreviate(self, word: str, k: int) -> str:
        return word if k>=len(word)-2 else word[:k]+str(len(word)-k-1)+word[-1]

wordDict = ['like', 'got', 'internal', 'me', 'internet', 'interval', 'intension', 'face', 'intrusion']
res = Solution().wordsAbbreviation(wordDict)
print(res)