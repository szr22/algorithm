#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = [None for _ in range(k)]
        cnt = 0
        node = root
        while node:
            cnt+=1
            node = node.next
        numPerList = cnt//k
        rem = cnt%k

        for i in range(k):
            res[i] = root
            ave = numPerList
            if i<rem:
                ave += 1

            for _ in range(ave-1):
                root = root.next

            if not root:
                break
            tmp = root.next
            root.next = None
            root = tmp

        return res



# @lc code=end

