# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded)+1
        nxor = n%4
        res = [0]*n
        res[0] = 0 if nxor==3 else 1
        for i in range(1,n,2):
            res[0]^=encoded[i]
        for i in range(1,n):
            res[i]=res[i-1]^encoded[i-1]
        return res