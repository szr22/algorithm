#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        stack = []
        for p in pathList:
            if not p or p=='.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)

# @lc code=end

path = "/a//b////c/d//././/.."
path = "/a/../../b/../c//.//"
path = "/a/./b/../../c/"
res = Solution().simplifyPath(path)
print(res)