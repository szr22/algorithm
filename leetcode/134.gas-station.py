#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        cur = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            cur += gas[i]-cost[i]
            if cur<0:
                start = i+1
                cur = 0
        if total<0:
            return -1
        return start


    def canCompleteCircuitBack(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        mx = -1
        start = 0
        for i in range(len(gas)-1, -1, -1):
            total += gas[i]-cost[i]
            if total>mx:
                start = i
                mx = total
        if total<0:
            return -1
        return start
# @lc code=end

