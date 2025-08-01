# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}
        def dfs(i,su):
            if (i,su) in mem:
                return mem[(i,su)]
            if i == n:
                if su == 0:
                    return 1
                else:
                    return 0
            ans = dfs(i+1,su+nums[i]) + dfs(i+1,su-nums[i])
            mem[(i,su)] = ans
            return ans
        return dfs(0,target)