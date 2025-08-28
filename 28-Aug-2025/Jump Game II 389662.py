# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dp(i):
            if i >= n - 1:
                return 0
            
            if cache[i] == -1:
                smallest = float('inf')
                for j in range(1, nums[i] + 1):
                    smallest = min(smallest, 1 + dp(i + j))
                
                cache[i] = smallest
            return cache[i]
        return dp(0)