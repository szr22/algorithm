#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.nums = nums
        return self.mergeSortAndCnt(0, len(nums)-1)

    def mergeSortAndCnt(self, start, end):
        if start>=end:
            return 0
        mid = (start+end)//2
        res = (
            self.mergeSortAndCnt(start, mid)
            + self.mergeSortAndCnt(mid+1, end)
        )
        i = start
        j = mid+1
        while i<=mid:
            while j<=end and self.nums[i] > self.nums[j]*2:
                j+=1
            i+=1
            res += j-(mid+1)

        self.merge(start, mid, end)
        return res

    def merge(self, start, mid, end):
        n1 = mid-start+1
        n2 = end-mid
        l1, l2 = [], []
        for i in range(n1):
            l1.append(self.nums[start+i])
        for i in range(n2):
            l2.append(self.nums[mid+1+i])

        i, j = 0, 0

        for k in range(start, end+1):
            if j>=n2 or (i<n1 and l1[i]<=l2[j]):
                self.nums[k] = l1[i]
                i+=1
            else:
                self.nums[k] = l2[j]
                j+=1

    def reversePairsFast(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return self.mergesort(nums)[1]


    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums, 0
        m = len(nums)//2
        left, countl = self.mergesort(nums[:m])
        right, countr = self.mergesort(nums[m:])
        count = countl + countr
        for r in right:
            temp = len(left) - bisect.bisect(left, 2*r)
            if temp == 0:
                break
            count += temp

        return sorted(left+right), count

# @lc code=end

