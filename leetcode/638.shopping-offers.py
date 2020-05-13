#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#
from typing import List
# @lc code=start
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # res = sum([price[i]*needs[i] for i in range(len(price))])
        res = sum([(v * price[i]) for i,v in enumerate(needs)])

        for coupon in special:
            # remains = self.applyCoupon(coupon, needs)
            # if not remains:
            #     continue
            # res = min(
            #     res,
            #     self.shoppingOffers(price, special, remains) + coupon[-1]
            # )
            if self.isValid(coupon, needs):
                remains = [need-coupon[i] for i, need in enumerate(needs)]
                res = min(
                    res,
                    self.shoppingOffers(price, special, remains) + coupon[-1]
                )

        return res

    def applyCoupon(self, coupon, needs):
        remains = [0 for _ in range(len(needs))]
        for i, need in enumerate(needs):
            if coupon[i] > need:
                return []
            remains[i] = need-coupon[i]
        return remains

    def isValid(self, coupon, needs):
        for i, need in enumerate(needs):
            if need<coupon[i]:
                return False
        return True


# @lc code=end

price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]

res = Solution().shoppingOffers(price, special, needs)
print(res)