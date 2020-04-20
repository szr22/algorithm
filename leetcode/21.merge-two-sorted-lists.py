#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        res = ListNode(-1)
        cur = res

        while l1 and l2:
            new_node = None
            if l1.val > l2.val:
                new_node = ListNode(l2.val)
                l2 = l2.next
            else:
                new_node = ListNode(l1.val)
                l1 = l1.next
            cur.next = new_node
            cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

# @lc code=end

