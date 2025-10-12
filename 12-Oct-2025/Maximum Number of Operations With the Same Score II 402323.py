# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def solve(sum_val, first, last):
            if first >= last:
                return 0            
            if dp[first][last] != -1:
                return dp[first][last]
            
            ans = 0            
            if sum_val == nums[first] + nums[first + 1]:
                ans = max(ans,1 + solve(sum_val, first + 2, last))
            
            if sum_val == nums[last] + nums[last - 1]:
                ans = max(ans,1 + solve(sum_val, first, last - 2))
            
            if sum_val == nums[first] + nums[last]:
                ans = max(ans,1 + solve(sum_val, first + 1, last - 1))

            dp[first][last] = ans
            return dp[first][last]
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]
        a = solve(nums[0] + nums[1], 0, n-1)

        dp = [[-1] * n for _ in range(n)]
        b = solve(nums[0] + nums[n-1], 0, n-1)

        dp = [[-1] * n for _ in range(n)]
        c = solve(nums[n-2] + nums[n-1], 0, n-1)

        return max(a, max(b, c))