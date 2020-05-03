#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#
from typing import List
from collections import Counter
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.cnt = Counter()
        self.maxCnt = 0
        self.res = []
        self.helper(root)
        # for n, c in self.cnt.items():
        #     if c == self.maxCnt:
        #         res.append(n)
        return self.res

    def helper(self, note):
        if not note:
            return 0
        left = self.helper(note.left)
        right = self.helper(note.right)
        total = left+right+note.val
        self.cnt[total] += 1
        if self.cnt[total]>=self.maxCnt:
            if self.cnt[total]>self.maxCnt:
                self.res = []
            self.res.append(total)
            self.maxCnt = self.cnt[total]
        # self.maxCnt = max(self.maxCnt, self.cnt[total])
        return total


# @lc code=end

