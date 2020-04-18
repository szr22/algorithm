#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

from typing import List
from collections import Counter, deque
import string

# @lc code=start
class Solution:
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList:
            return 0
        word_set = set(wordList)
        min_path_len = float('inf')
        queue = deque([([beginWord], beginWord)])
        visited = set()
        valid_path = deque()
        while queue:
            path, last_word = queue.popleft()
            if last_word not in visited:
                visited.add(last_word)
                for word in word_set:
                    if self.check_distance(word, last_word) == 1:
                        path.append(word)
                        if word == endWord:
                            min_path_len = min(min_path_len, len(path))
                            valid_path.append(path.copy())
                        queue.append((path.copy(), word))
                        path.pop()
        return min_path_len if min_path_len != float('inf') else 0

    def check_distance(self, word1: str, word2: str) -> int:
        dist_count = Counter(word1) - Counter(word2)
        dist = 0
        for v in dist_count.values():
            dist += v
        return dist

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        word_set = set(wordList)
        min_path_len = float('inf')
        queue = deque([([beginWord], beginWord)])
        visited = set()
        while queue:
            path, node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for idx in range(len(endWord)):
                    for lett in string.ascii_lowercase:
                        new_word = node[:idx] + lett + node[idx+1:]
                        if new_word == endWord and endWord in word_set:
                            min_path_len = min(len(path)+1, min_path_len)
                        else:
                            if new_word not in path and new_word in word_set:     
                                path.append(new_word)
                                queue.append((path.copy(), new_word))
                                path.pop()
        return min_path_len if min_path_len != float('inf') else 0

# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog", "het"]


# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]

# beginWord = "leet"
# endWord = "code"
# wordList = ["lest","lost","leet","lose","code","lode","rode"]

res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)


# print(Solution().check_distance('hit', 'zib'))
