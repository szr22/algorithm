"""
Convert a BST to a sorted circular doubly-linked list in-place.
Think of the left and right pointers as synonymous
to the previous and next pointers in a doubly-linked list.

Input: {4,2,5,1,3}
        4
       /  \
      2   5
     / \
    1   3
Output: "left:1->5->4->3->2  right:1->2->3->4->5"
Explanation:
Left: reverse output
Right: positive sequence output

Input: {2,1,3}
        2
       /  \
      1   3
Output: "left:1->3->2  right:1->2->3"
"""

from TreeNode import TreeNode, Tree
from typing import List


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

head = Node(-1)
cur = head

class Solution:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def buildList(self, root):
        self.inorder(root)
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        tmp = Node(root.val)
        self.tail.next = tmp
        tmp.prev = self.tail
        self.tail = self.tail.next

        self.inorder(root.right)

    def printList(self):
        # while self.head:
        for _ in range(5):
            print(self.head.val)
            self.head = self.head.next

        print()

        # while self.tail:
        for _ in range(5):
            print(self.tail.val)
            self.tail = self.tail.prev


sol = Solution()
sol.buildList(root)
print()
sol.printList()

# BinaryTree tree = new BinaryTree();
root = TreeNode(10)
root.left = TreeNode(12)
root.right = TreeNode(15)
root.left.left = TreeNode(25)
root.left.right = TreeNode(30)
root.right.left = TreeNode(36)

sol = Solution()
sol.buildList(root)
print()
sol.printList()