"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2
"""

class Solution:
    def longestConsecutive(self, root):
        if not root:
            return 0

        self.res = 0
        self.cur = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, val):
        if not root:
            return
        if root.val == val+1:
            self.cur +=1
        else:
            # re-init
            self.cur = 1

        self.res = max(self.res, self.cur)
        self.dfs(root.left, root.val)
        self.dfs(root.right, root.val)

    