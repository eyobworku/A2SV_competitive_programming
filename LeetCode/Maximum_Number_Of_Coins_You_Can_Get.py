class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        res = 0
        for i in range(n//3):
            res += piles[n-2*i-2]
        return res