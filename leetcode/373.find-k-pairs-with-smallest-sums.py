#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairsStraight(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return solution

        n1, n2 = len(nums1), len(nums2)
        res = []
        heap = [(0x7FFFFFFF, None, None)]
        idx2 = 0
        while len(res) < min(k, n1 * n2):
            if idx2<n2:
                total, i, j = heap[0]
                if nums2[idx2]+nums1[0]<total:
                    for idx1 in range(n1):
                        heapq.heappush(heap,(nums1[idx1]+nums2[idx2], idx1, idx2))
                    idx2 += 1
                total, i, j = heapq.heappop(heap)
                res.append((nums1[i], nums2[j]))
        return res

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs

# @lc code=end

