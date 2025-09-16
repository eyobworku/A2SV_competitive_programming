# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac = 0
        for i in range(1, n+1):
            if n%i == 0:
                fac += 1
                if fac==k:
                    return i
        return -1