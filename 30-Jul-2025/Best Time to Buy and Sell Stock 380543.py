# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        b,s = prices[0],0
        for i in range(1,len(prices)):
            if prices[i] < b:
                b = prices[i]
                s = prices[i]
            if prices[i] > s:
                s = prices[i]
            res = max(res,s-b)
        return res