"""
Given a set of words (without duplicates), find all word squares you can build from them.
A sequence of words forms a valid word square if the kth row and column read the exact same string,
where 0 ≤ k < max(numRows, numColumns).
For example, the word sequence ["ball","area","lead","lady"]
forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:
Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]
"""

from typing import List
from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = dict()

    def buildTrie(self, words):
        for word in words:
            # self.addNode function
            cur = self.root
            for char in word:
                if char not in cur:
                    cur[char] = dict()
                cur = cur[char]

    def search(self, prefix):
        cur = self.root
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return None
        return cur

    def __repr__(self):
        return str(self.root)

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []

        self.trie = Trie()
        self.trie.buildTrie(words)

        res = []
        for word in words:
            curSquare = [word]
            self.searchSubSqueres(len(word), curSquare, res)
        return res

    def searchSubSqueres(self, squareLen, curSquare, res):
        if len(curSquare) == squareLen:
            res.append(curSquare.copy())
            return
        prefix = self.getPrefix(curSquare)
        prefixNode = self.trie.search(prefix)
        if not prefixNode:
            return

        childrenWords = []
        self.getChildren(prefixNode, prefix, childrenWords)
        for child in childrenWords:
            curSquare.append(child)
            self.searchSubSqueres(squareLen, curSquare, res)
            curSquare.pop()

    def getPrefix(self, curSquare) -> str:
        prefix = ''
        idx = len(curSquare)
        for word in curSquare:
            prefix+=word[idx]
        return prefix

    def getChildren(self, prefixNode, prefix, childrenWords):
        if not prefixNode:
            childrenWords.append(prefix)
        for char, node in prefixNode.items():
            self.getChildren(node, prefix+char, childrenWords)



words = ["abat","baba","atan","atal"]
res = Solution().wordSquares(words)
print(res)

