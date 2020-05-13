#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.data = [0 for _ in range(n)]
        self.bit = [0 for _ in range(n+1)]
        for i in range(n):
            self.update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        diff = val - self.data[i]
        j=i+1
        while j < len(self.bit):
            self.bit[j] += diff
            j += (j&-j)
        self.data[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.getSum(j+1)-self.getSum(i)

    def getSum(self, i: int) -> int:
        total = 0
        j = i
        while j>0:
            total += self.bit[j]
            j -= (j&-j)
        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

class NumArrayStraight:

    def __init__(self, nums: List[int]):
        self.data = nums

    def update(self, i: int, val: int) -> None:
        self.data[i] = val

    def sumRange(self, i: int, j: int) -> int:
        total = 0
        for k in range(i, j+1):
            total += self.data[k]

        return total

class NumArraySegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0 for _ in range(self.n*2)]
        self.buildTree(nums)

    def buildTree(self, nums):
        for i in range(self.n, self.n*2):
            self.tree[i] = nums[i-self.n]
        for i in range(self.n-1, -1, -1):
            self.tree[i] = self.tree[i*2]+self.tree[i*2+1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i>0:
            self.tree[i//2] = self.tree[i]+self.tree[i^1]
            i //=2

    def sumRange(self, i: int, j: int) -> int:
        total = 0
        i, j = i+self.n, j+self.n
        while i<=j:
            if i&1 == 1:
                total += self.tree[i]
                i += 1
            if j&1 == 0:
                total += self.tree[j]
                j -= 1
            i //= 2
            j //= 2

        return total