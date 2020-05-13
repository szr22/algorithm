#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        self.res = False
        eps = 0.001

        self.helper(nums, eps)
        return self.res

    def helper(self, nums, eps):
        if self.res:
            return
        if len(nums) == 1:
            if abs(nums[0] - 24) < eps:
                self.res = True
                return

        for i in range(len(nums)):
            for j in range(0, i):
                p = nums[i]
                q = nums[j]

                tmp = [p+q, p-q, q-p, p*q]
                if p>eps:
                    tmp.append(q/p)
                if q>eps:
                    tmp.append(p/q)

                nums.pop(i)
                nums.pop(j)

                for num in tmp:
                    nums.append(num)
                    self.helper(nums, eps)
                    if self.res:
                        return
                    nums.pop()

                nums.insert(j, q)
                nums.insert(i, p)


# @lc code=end

