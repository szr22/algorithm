#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

from collections import defaultdict
# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [(-1, 0)]  # (current level, length of the current path)
        foundFile = False
        nextLevel = currLevel = currLen = maxLen = 0
        i, n = 0, len(input)
        while i < n:
            c = input[i]
            if c == '\n':
                # Found a file in the previous item, calculate its path length.
                if foundFile:
                    maxLen = max(maxLen, currLen)
                    foundFile = False

                # Check the level for the next item.
                nextLevel = 0
                while input[i + 1] == '\t':
                    nextLevel += 1
                    i += 1

                if currLevel < nextLevel:  # Go down.
                    currLen += 1  # '/' takes one pisition in the path.
                    stack.append((currLevel, currLen))
                else:  # Stay on the same or go up.
                    while stack[-1][0] >= nextLevel:
                        stack.pop()

                    currLen = stack[-1][-1]

                currLevel = nextLevel
            else:
                if c == '.':
                    foundFile = True

                currLen += 1

            i += 1  # Process the next char.

        if foundFile:  # Process the last file if any.
            maxLen = max(maxLen, currLen)

        return maxLen

# @lc code=end

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
res = Solution().lengthLongestPath(input)
print(res)