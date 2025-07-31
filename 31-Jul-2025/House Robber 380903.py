# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dpf(i):
            if i == 0: return nums[0]
            if i == 1: return max(nums[0],nums[1])
            if dp[i] != -1:
                return dp[i]
            dp[i] =  max(dpf(i-1),dpf(i-2) + nums[i])
            return dp[i]
        
        return dpf(n-1)