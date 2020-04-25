#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
from collections import defaultdict, OrderedDict
import heapq
import datetime
# @lc code=start

class LRUCache(object):
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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

# obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

class LRUCacheBad:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = defaultdict(int)
        self.queue =[]

    def get(self, key: int) -> int:
        if key in self.hashMap.keys():
            # reset queue order for key
            item = self.hashMap[key]
            self.queue.remove(item)
            self.queue.append(item)
            return item[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap.keys():
            item = self.hashMap[key]
            self.queue.remove(item)
        elif len(self.hashMap) == self.capacity:
            item = self.queue.pop(0)
            self.hashMap.pop(item[0])
        self.queue.append([key,value])
        self.hashMap[key]=self.queue[-1]

obj = LRUCache(2)
print(obj.get(2))
obj.put(2,6)
print(obj.get(1))
obj.put(1,5)
obj.put(1,2)
print(obj.get(1))
print(obj.get(2))