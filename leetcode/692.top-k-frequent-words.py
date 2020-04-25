#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

from collections import Counter
import heapq
from operator import itemgetter
from typing import List
import operator

# @lc code=start

class CustomerCounter(Counter):
    def sort_key(self, key):
        return -key[1], key[0]

    def most_common(self, n=None):
        if n is None:
            return sorted(self.items(), key=operator.itemgetter(1, 0), reverse=True)
        return heapq.nsmallest(n, self.items(), key=self.sort_key)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = CustomerCounter(words)
        top_k_freq = word_counter.most_common(k)
        return [word for (word, _) in top_k_freq]

# @lc code=end

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

res = Solution().topKFrequent(words, k)
print(res)

# using trie and min-heap
# https://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/