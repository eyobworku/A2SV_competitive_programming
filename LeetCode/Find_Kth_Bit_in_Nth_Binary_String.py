class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n,k):
            if n==1: return False
            l = (2**n)//2
            if k==l:
                return True
            elif k>l:
                return not solve(n-1,l-(k%l))
            else:
                return solve(n-1,k)
        return '1' if solve(n,k) else '0'
        
        