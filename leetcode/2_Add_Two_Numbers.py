# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        cur = None
        carry = 0
        while l1 and l2:
            curVal = l1.val+l2.val+carry
            if curVal>9:
                carry = 1
                curVal%=10
            else:
                carry = 0
            if res:
                cur.next = ListNode(curVal)
                cur = cur.next
            else:
                cur = ListNode(curVal)
                res = cur
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curVal = l1.val+carry
            if curVal>9:
                carry = 1
                curVal%=10
            else:
                carry = 0
            if res:
                cur.next = ListNode(curVal)
                cur = cur.next
            else:
                cur = ListNode(curVal)
                res = cur
            l1 = l1.next
        while l2:
            curVal = l2.val+carry
            if curVal>9:
                carry = 1
                curVal%=10
            else:
                carry = 0
            if res:
                cur.next = ListNode(curVal)
                cur = cur.next
            else:
                cur = ListNode(curVal)
                res = cur
            l2 = l2.next
        if carry>0:
            cur.next = ListNode(carry)
            
        return res


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

res = Solution().addTwoNumbers(l1, l2)

while res:
    print(res.val)
    res = res.next