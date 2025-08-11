# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ss = sum(nums)
        if ss%2: return False
        memo = {}

        def dfs(i,su):
            if (i,su) in memo:
                return memo[(i,su)]
            if i < 0 or su < 0:
                return False
            if su == 0:
                return True
                
            if i > 0 and dfs(i-1,su - nums[i]) or dfs(i-1,su):
                return True
            memo[(i,su)] = False
            return memo[(i,su)]

        return dfs(len(nums)-1,ss//2)

