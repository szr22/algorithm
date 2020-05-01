#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head

        while pre.next and pre.next.next:
            nxt = pre.next.next
            pre.next.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            pre = nxt.next

        return dummy.next

# @lc code=end
