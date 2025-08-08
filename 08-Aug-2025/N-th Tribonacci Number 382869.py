# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        f,s,t = 0,1,1
        if n < 3: return 1 if n==2 else n
        for _ in range(n-2):
            temp = f + s + t
            f,s,t = s,t,temp
        return t