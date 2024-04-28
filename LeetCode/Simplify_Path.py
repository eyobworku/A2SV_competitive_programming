class Solution:
    def simplifyPath(self, path: str) -> str:
        slashed = path.split('/')
        stack = []
        for x in slashed:
            if x in ('','.'):
                continue
            elif x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        
        return '/'+'/'.join(stack)
        