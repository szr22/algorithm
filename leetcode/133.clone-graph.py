#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphRec(self, node: 'Node') -> 'Node':
        self.hashmap = {}
        return self.createClone(node)

    def createClone(self, node):
        if not node:
            return None
        if node in self.hashmap:
            return self.hashmap[node]
        clone = Node(node.val)
        self.hashmap[node] = clone
        for nei in node.neighbors:
            clone.neighbors.append(self.createClone(nei))
        return clone

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        hashmap = {}
        queue = [node]
        cloneNode = Node(node.val)
        hashmap[node] = cloneNode
        while queue:
            curNode = queue.pop()
            for nei in curNode.neighbors:
                # visited before
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    queue.append(nei)
                hashmap[curNode].neighbors.append(hashmap[nei])
        return cloneNode

# @lc code=end

