# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        while True: 
            nn, sm = n, 0
            for f in range(2, nn+1): 
                while nn % f == 0: 
                    nn //= f
                    sm += f
            if sm == n:
                break 
            n = sm 
        return n
