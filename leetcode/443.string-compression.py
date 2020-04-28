#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import List
import itertools
# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0
        for c, g in itertools.groupby(chars):
            x = len(list(g))
            chars[k] = c
            k += 1
            if x > 1:
                for i in str(x):
                    chars[k] = i
                    k += 1
        return k

    def compressFail(self, chars: List[str]) -> int:
        n = len(chars)
        if n < 2:
            return chars
        i = 0
        # res = ''
        while i < (len(chars)-1):
            cnt = 1
            while i<(len(chars)-1) and chars[i]==chars[i+1]:
                cnt += 1
                chars.pop(i+1)
            if cnt>1:
                # res += chars[i]+str(cnt)
                chars = chars[:i+1]+list(str(cnt))+chars[i+1:]
                i+=1
            i+=1
        res = chars
        print(res)
        return len(res)

# @lc code=end
chars = ["a","a", "d", "b","b","c","c","c", 'd']
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
res = Solution().compress(chars)
print(res)
