#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashMap:
            return False
        self.nums.append(val)
        self.hashMap[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashMap:
            return False
        last = self.nums[-1]
        self.hashMap[last] = self.hashMap[val]
        self.nums[self.hashMap[val]] = last
        self.nums.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0,len(self.nums)-1)
        return self.nums[idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1)
param_2 = obj.remove(2)
print(param_2)
param_3 = obj.getRandom()
print(param_3)
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
