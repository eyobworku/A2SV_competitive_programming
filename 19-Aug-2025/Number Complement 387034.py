# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bi = bin(num)[::-1]
        res=0
        for i in range(len(bi)-2):
            if bi[i]=='0':
                res+=2**i
        return res