#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

from typing import List

# @lc code=start
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9]+', ' ', paragraph)
        word_list = paragraph.split()

        word_map = {}
        max_count = 0
        for word in word_list:
            if word in word_map:
                word_map[word] += 1
                max_count = max(max_count, word_map[word])
                continue

            if word not in banned:
                word_map[word] = 1
                max_count = max(max_count, word_map[word])

        # res = []
        for k, v in word_map.items():
            if v == max_count:
                # res.append(k)
                return k
        # return res


# @lc code=end

paragraph = "Bob hit a ball,,,,,, the hit BALL's flew far after it was hit."
banned = ["hit"]


res = Solution().mostCommonWord(paragraph, banned)
print(res)