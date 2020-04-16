class Solution:
    def checkValidStringTle(self, s: str) -> bool:
        return self.check_valid_string(s, [])

    def check_valid_string(self, s, stack) -> bool:
        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    return False
            elif c == '*':
                return (
                    self.check_valid_string(s[i+1:], stack+[]) or
                    self.check_valid_string(s[i+1:], stack+['(']) or
                    (len(stack)>0 and self.check_valid_string(s[i+1:], stack[:-1]))
                )
        return not stack

    def checkValidString(self, s):
        c_min = c_max = 0
        for i in s:
            if i == '(':
                c_max += 1
                c_min += 1
            if i == ')':
                c_max -= 1
                c_min = max(c_min - 1, 0)
            if i == '*':
                c_max += 1
                c_min = max(c_min - 1, 0)
            if c_max < 0:
                return False
        return c_min == 0

res = Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((*)*)())**)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
print(res)