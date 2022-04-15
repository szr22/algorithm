#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        def decodings(s, idx, encodings, memo)-> int:
            if idx >= len(s):
                return 1

            if idx in memo:
                return memo[idx]

            count = 0

            if s[idx:idx+1] in encodings:
                count += decodings(s, idx+1, encodings, memo)

            if idx+2 <= len(s) and s[idx:idx+2] in encodings:
                count += decodings(s, idx+2, encodings, memo)

            memo[idx] = count
            return count


        encoding = {}
        for i in range(1, 27):
            encoding[str(i)] = chr(ord('A') + i - 1)

        return decodings(s, 0, encoding, {})

# @lc code=end

