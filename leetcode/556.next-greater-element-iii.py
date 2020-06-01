#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        sList = list(str(n))
        idx = -1
        for i in range(len(sList)-1, 0, -1):
            if sList[i-1]<sList[i]:
                idx = i-1
                break
        if idx<0:
            return -1
        diff = float('Inf')
        swapped_idx = idx
        for i in range(idx+1, len(sList)):
            if sList[i]>sList[idx] and int(sList[i])-int(sList[idx])<diff:
                diff = int(sList[i])-int(sList[idx])
                swapped_idx = i

        sList[idx], sList[swapped_idx] = sList[swapped_idx], sList[idx]

        res = ''.join(sList[:idx+1]+sorted(sList[idx+1:]))
        if int(res)<2**31:
            return res
        return -1
# @lc code=end

