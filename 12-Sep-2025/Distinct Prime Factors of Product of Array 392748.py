# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        facSet = set()
        def factor(n):
            d = 2
            while d * d <= n:
                while n%d==0:
                    facSet.add(d)
                    n//=d
                d+=1
            if n>1:
                facSet.add(n)
        for n in nums:
            factor(n)

        return len(facSet)
