#
# @lc app=leetcode id=1044 lang=python3
#
# [1044] Longest Duplicate Substring
#
from functools import reduce
# @lc code=start
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        def check(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo+hi+1)//2
            pos = check(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
# @lc code=end



MODULO = 100000000487  # prime

class SolutionBetter:
    def longestDupSubstring(self, S: str) -> str:
        ords = bytes(ord(c) - ord('a') for c in S)

        cumulatives = [0]
        for o in ords:
            cumulatives.append(
                ( cumulatives[-1] * 26 + o) % MODULO
            )

        def _duplicate(length):
            MULT = pow(26, length + 1, MODULO)
            hsh = cumulatives[length + 1]
            seen = {hsh}
            for start in range(1, len(S) - length):
                hsh = ((26 * hsh - MULT * ords[start - 1]) + ords[start + length]) % MODULO
                if hsh in seen:
                    return start
                seen.add(hsh)
            return None

        best = None
        best_len = -1

        left = 0
        right = len(S) - 1

        while right - left >= 2:
            middle = (left + right) // 2
            cand = _duplicate(middle)
            cand_len = middle + 1
            if cand is not None:
                if cand_len > best_len:
                    best = cand
                    best_len = cand_len

                left = middle + 1
            else:
                right = middle - 1

        if best_len < left + 1:
            new_cand = _duplicate(left)
            if new_cand is not None:
                best = new_cand
                best_len = left + 1
                new_cand = _duplicate(right)
                if new_cand is not None:
                    best = new_cand
                    best_len = right + 1

        if best is None:
            return ''

        return S[best:best + best_len]