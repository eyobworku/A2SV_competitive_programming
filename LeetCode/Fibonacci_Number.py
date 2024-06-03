class Solution:
    def fib(self, n: int) -> int:
        if n ==1 or n==0:
            return n
        
        f ,s = 0,1
        for _ in range(1,n):
            t = s
            s +=f
            f = t
        return s