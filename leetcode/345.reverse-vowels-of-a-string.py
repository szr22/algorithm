#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowelsStraight(self, s: str) -> str:
        start, end = 0, len(s)-1
        sList = list(s)
        vowels = set(["a", "e", "i", "o", "u"])
        while start<end:
            if sList[start].lower() not in vowels:
                start+=1
            elif sList[end].lower() not in vowels:
                end -= 1
            else:
                sList[start], sList[end] = sList[end], sList[start]
                start+=1
                end-=1
        return "".join(sList)

    def reverseVowels(self, s):
        # return re.sub('(?i)[aeiou]', lambda m, v=re.findall('(?i)[aeiou]', s): v.pop(), s)
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
# @lc code=end
s = "leetcode"
s = ""
res = Solution().reverseVowels(s)
print(res)

