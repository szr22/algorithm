"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue,
and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
"""
from typing import List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def instert(self, val):
        node = Node(val)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.count += 1
        return node

    def remove(self, node):
        pre, nxt = node.prev, node.next
        node.prev.next = nxt
        node.next.prev = pre
        self.count -= 1

    def isEmpty(self):
        return self.count == 0

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dll = DoubleLinkedList()
        self.numDict = dict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        print(self.dll.head.next.val)
        if self.dll.isEmpty():
            return -1
        # print(self.dll.head.next.val)
        return self.dll.head.next.val


    def add(self, value: int) -> None:
        if value in self.numDict:
            if self.numDict[value]:
                self.dll.remove(self.numDict[value])
                self.numDict[value] = None
        else:
            node = self.dll.instert(value)
            self.numDict[value] = node
        print(self.dll.count)

# nums = [2,3,5]
# firstUnique = FirstUnique(nums)
# firstUnique.showFirstUnique()
# firstUnique.add(5)
# firstUnique.showFirstUnique()
# firstUnique.add(2)
# firstUnique.showFirstUnique()
# firstUnique.add(3)
# firstUnique.showFirstUnique()

["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]

nums = [7,7,7,7,7,7]
firstUnique = FirstUnique(nums)
firstUnique.showFirstUnique()
firstUnique.add(7)
firstUnique.add(3)
firstUnique.add(3)
firstUnique.add(7)
firstUnique.add(17)
firstUnique.showFirstUnique()

import collections
class FirstUnique2:
    def __init__(self, nums: List[int]):
        self.d = collections.OrderedDict()
        for num in nums:
            self.d[num] = self.d.get(num, 0) + 1
        self.removed = set()
        for key in list(self.d.keys()):
            if self.d[key] > 1:
                self.removed.add(key)
                self.d.pop(key)
        # print(self.d)
        # print(next(iter(self.d)))

    def showFirstUnique(self) -> int:
        return next(iter(self.d)) if self.d else -1


    def add(self, value: int) -> None:
        if value not in self.removed:
            if value in self.d:
                self.d.pop(value)
                self.removed.add(value)
            else:
                self.d[value] = 1
