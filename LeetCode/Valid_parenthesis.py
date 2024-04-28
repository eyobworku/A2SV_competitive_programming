class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for x in s:
            if x in ('(','{','['):
                stack.append(x)
            elif stack and par[x] == stack[-1]:
                stack.pop()

            else:
                return False
        return not stack