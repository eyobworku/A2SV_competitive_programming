# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        d = 2
        while d*d <= n:
            while n%d==0:
                res+=d
                n//=d
            d+=1
        if n > 1:
            res+=n
        return res