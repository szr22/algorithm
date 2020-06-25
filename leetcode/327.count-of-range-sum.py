#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
import bisect
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.sums = [0]*(n+1)
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)
    def lowbit(self, x):
        return x & -x
    def sum(self, x):
        res = 0
        while x>0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = nums[:]
        for x in range(len(sums)-1):
            sums[x+1] += sums[x]
        sortedSums = sorted(set(sums))
        ft = FenwickTree(len(sortedSums))
        res = 0
        for s in sums:
            left = bisect.bisect_left(sortedSums, s - upper)
            right = bisect.bisect_right(sortedSums, s - lower)
            res += ft.sum(right) - ft.sum(left) + (lower<=s<=upper)
            ft.add(bisect.bisect_right(sortedSums, s), 1)
        return res

    def countRangeSumMerge(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            sums[i+1] = sums[i]+nums[i]
        self.m = max(sums)
        return self.countAndMergeSort(sums, 0, len(nums), lower, upper)

    def countAndMergeSort(self, sums, start, end, lower, upper):
        if end-start == 0:
            return 0
        mid = (start+end)//2
        cnt = (
            self.countAndMergeSort(sums, start, mid, lower, upper)
            + self.countAndMergeSort(sums, mid+1, end, lower, upper)
        )
        x, y = start, start
        for i in range(mid+1, end+1):
            while x<=mid and sums[i]-sums[x] >= lower:
                x+=1

            while y<=mid and sums[i]-sums[y] > upper:
                y+=1
            cnt += x-y

        mem =sums[start:end+1]

        s, e = start, mid+1
        for i in range(start, end+1):
            x = mem[s-start] if s <= mid else self.m
            y = mem[e-start] if e <= end else self.m
            if x<y:
                s += 1
            else:
                e += 1
            sums[i] = min(x,y)

        return cnt

# @lc code=end

