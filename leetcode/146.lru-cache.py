#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from collections import defaultdict, OrderedDict
import heapq
import datetime
# @lc code=start

class LRUCache2(object):
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            while len(self.od) >= self.cap:
                self.od.popitem(False)
            self.od[key] = value

class DoubleLinkedNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nxt = None
        self.pre = None

    def show(self):
        while self:
            print(self.val)
            self = self.nxt

class LRUCache(object):
    def __init__(self, capacity):
        INF = float('inf')
        self.cap = capacity
        self.dic = {}
        self.double_list_size = 0
        self.dummy_head = DoubleLinkedNode(INF, INF)
        self.dummy_tail = DoubleLinkedNode(INF, INF)
        self.dummy_head.nxt = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, key):
        if key not in self.dic:
            return -1
        else:
            self.move_to_end(key)
            return self.dic[key].val

    def move_to_end(self, key):
        cur_node = self.dic[key]

        cur_node.pre.nxt = cur_node.nxt
        cur_node.nxt.pre = cur_node.pre

        tail = self.dummy_tail.pre
        cur_node.nxt = self.dummy_tail
        self.dummy_tail.pre = cur_node

        tail.nxt = cur_node
        cur_node.pre = tail

    def put(self, key, value):
        if key in self.dic:
            self.move_to_end(key)
            self.dic[key].val = value

        else:
            if self.double_list_size >= self.cap:

                head = self.dummy_head.nxt
                del self.dic[head.key]
                self.double_list_size -= 1

                head = head.nxt
                head.pre = self.dummy_head
                self.dummy_head.nxt = head

            node = DoubleLinkedNode(key, value)
            self.dic[key] = node
            self.double_list_size += 1


            tail = self.dummy_tail.pre
            node.pre = tail
            node.nxt = self.dummy_tail

            tail.nxt = node
            self.dummy_tail.pre = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

# obj = LRUCache(2)
# print(obj.get(2))
# obj.put(2,6)
# print(obj.get(1))
# obj.put(1,5)
# obj.put(1,2)
# print(obj.get(1))
# print(obj.get(2))

pr(obj.dummy_head)