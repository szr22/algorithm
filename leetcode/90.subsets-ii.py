#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDupSlow(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def back_track(idx, track):
            res.append(track)
            if idx >= len(nums):
                return
            num_set = set()

            for i in range(idx,len(nums)):
                if nums[i] not in num_set:
                    num_set.add(nums[i])
                    back_track(i+1,track+(nums[i],))

        res=[]
        back_track(0,tuple())
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        self.result = []
        def backtrack(i, track):
            self.result.append(track.copy())
            for index in range(i, len(nums)):
                num = nums[index]
                if index > i and nums[index-1] == nums[index]:
                    continue
                track.append(num)
                backtrack(index+1, track)
                track.pop()

        backtrack(0,  [])
        return self.result

# @lc code=end

