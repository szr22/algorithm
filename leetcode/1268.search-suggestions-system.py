#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
from typing import List
from bisect import bisect_left, bisect_right
import collections


# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.words) < 3:
                node.words.append(word)

    def search(self, word):
        res = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words[:])
        remain = len(word) - len(res)
        for _ in range(remain):
            res.append([])
        return res

class Solution:
    def suggested_products_trie(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for word in products:
            trie.add(word)
        return trie.search(searchWord)

    def suggested_products_simple(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Finds all words per prefix + sort with only top 3 words.
        wordsPerPrefix = collections.defaultdict(list)
        def findWords(x, length):
            for word in products:
                if word[:length] == x:
                    wordsPerPrefix[x].append(word)

            wordsPerPrefix[x] = sorted(wordsPerPrefix[x])[:3]

        # Iterate and call findWords len(searchWord) times
        end, maxEnd = 1, len(searchWord)
        while end != maxEnd + 1:
            findWords(searchWord[:end], end)
            end += 1

        # return the list of lists.
        return wordsPerPrefix.values()

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        fake_words = [i + "#" for i in products]
        res = []
        for i in range(len(searchWord)):
            x = bisect_left(fake_words, searchWord[:i+1]+chr(0))
            y = bisect_right(fake_words, searchWord[:i+1]+chr(127))

            res.append(products[x:y][:3])
        return res
# @lc code=end

# products = ["mobile","mouse","moneypot","monitor","mousepad", 'macker']
# searchWord = "mouse"

products=["tatiana"]
searchWord="havana"

products = ["havana"]
searchWord = "havana"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

res = Solution().suggestedProducts(products, searchWord)
print(res)
