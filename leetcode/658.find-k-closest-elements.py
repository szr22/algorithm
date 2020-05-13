#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
from typing import List
# @lc code=start
class Solution:
    def findClosestElementsStraight(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr)-1
        while end-start >= k:
            # if equal choose the small one, which means to exclude larger one
            if x-arr[start] <= arr[end]-x:
                end -= 1
            else:
                start += 1
            print(start, end)
        return arr[start:end+1]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr)-k
        while start<end:
            mid = (start+end)//2
            if x - arr[mid] > arr[mid+k] - x:
                start = mid+1
            else:
                end = mid
        return arr[start: start+k]

# @lc code=end

arr = [0,0,0,1,3,5,6,7,8,8]
k = 2
x = 2

# arr = [1,2,3,4,5]
# k=4
# x=-1

# arr = [1,2,3,4,5]
# k=4
# x=3

res = Solution().findClosestElements(arr, k, x)
print(res)