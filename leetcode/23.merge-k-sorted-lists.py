#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

from typing import List
import heapq

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class NodeIndex:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []
        n = len(lists)
        i=0
        for i in range(len(lists)):
            if not lists[i]:
                continue

            node = lists[i]
            heapq.heappush(heap, NodeIndex(node.val, i))
            node = node.next
            lists[i] = node

        res = ListNode(-1)
        cur = res

        while heap:
            node_idx = heapq.heappop(heap)
            cur.next = ListNode(node_idx.val)
            cur = cur.next

            if lists and lists[node_idx.idx]:
                node = lists[node_idx.idx]
                heapq.heappush(heap, NodeIndex(node.val, node_idx.idx))
                node = node.next
                lists[node_idx.idx] = node

        return res.next

# @lc code=end

