#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self.hashtable = {}
        node = head
        while node:
            new_node = self.create_node(node)
            new_node.next = self.create_node(node.next)
            new_node.random = self.create_node(node.random)
            node = node.next
        return self.hashtable[head]

    def create_node(self, node):
        if not node:
            return None

        if node in self.hashtable:
            return self.hashtable[node]
        else:
            new_node = Node(node.val)
            self.hashtable[node] = new_node
            return new_node
# @lc code=end

