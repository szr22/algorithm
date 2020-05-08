#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.is_same_tree(s, t):
            return True
        return (
            self.isSubtree(s.left, t)
            or self.isSubtree(s.right, t)
        )

    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        if s.val != t.val:
            return False

        return (
            self.is_same_tree(s.left, t.left)
            and self.is_same_tree(s.right, t.right)
        )

    def isSubtreeSerialize(self, s, t):
        oStrList1 = []
        oStrList2 = []

        self.serialize(s, oStrList1)
        self.serialize(t, oStrList2)
        return ('').join(oStrList2) in ('').join(oStrList1)

    def serialize(self, node, oStrList):
        if not node:
            oStrList.append(',#')
        else:
            oStrList.append(','+str(node.val))
            self.serialize(node.left, oStrList)
            self.serialize(node.right, oStrList)

# @lc code=end

# [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2] \n [1,null,1,null,1,null,1,null,1,null,1,2]
