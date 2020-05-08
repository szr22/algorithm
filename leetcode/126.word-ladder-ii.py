#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

from collections import defaultdict, deque
from typing import List

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList:
            return 0
        graph = self.build_graph(wordList)
        n = len(wordList[0])

        prev = defaultdict(set)
        queue = deque([beginWord])
        while queue and endWord not in prev:
            q_len = len(queue)
            new_prev = defaultdict(set)
            for _ in range(q_len):
                word = queue.popleft()
                for i in range(n):
                    word_pattern = f"{word[:i]}*{word[i+1:]}"
                    for next_word in graph[word_pattern]:
                        if next_word not in prev:
                            new_prev[next_word].add(word)
                            queue.append(next_word)
            print(new_prev)
            prev.update(new_prev)
            print(prev)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            print(res)
            res = [[p]+r for r in res for p in prev[r[0]]]
        return res


    def build_graph(self, wordList: List[str]) -> defaultdict(list):
        n = len(wordList[0])
        graph = defaultdict(list)
        for word in wordList:
            for i in range(n):
                word_pattern = f"{word[:i]}*{word[i+1:]}"
                graph[word_pattern].append(word)
        return graph


# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog", "het"]

def buildGrpah(wordList):
    # suppose all are in the same length
    n = len(wordList[0])
    graph = defaultdict(list)
    for word in wordList:
        for i in range(n):
            pattern = f'{word[:i]}*{word[i+1:]}'
            graph[pattern].append(word)
    return graph

graph = buildGrpah(wordList)

queue = [beginWord]
visited = defaultdict(set)
w_len = len(beginWord)

while queue and endWord not in visited:
    size = len(queue)
    visiting = defaultdict(set)

    for _ in range(size):
        word = queue.pop(0)
        for i in range(w_len):
            pattern = f'{word[:i]}*{word[i+1:]}'
            for next_word in graph[pattern]:
                if next_word not in visited:
                    queue.append(next_word)
                    visiting[next_word].add(word)
    visited.update(visiting)

res = [[endWord]]
while res and res[0][0] != beginWord:
    new_res =[]
    for r in res:
        for word in visited[r[0]]:
            new_res.append([word]+r)
    res = new_res
print(res)

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]

# beginWord = "leet"
# endWord = "code"
# wordList = ["lest","lost","leet","lose","code","lode","rode"]

# beginWord = "a"
# endWord = "c"
# wordList = ["a","b","c"]

res = Solution().findLadders(beginWord, endWord, wordList)
print(res)