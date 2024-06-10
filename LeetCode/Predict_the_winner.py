class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        def dfs(i, j):
            if i == j:
                return nums[i]
            if dp[i][j] != -1:
                return dp[i][j]
            leftDiff = nums[i] - dfs(i + 1, j)
            rightDiff = nums[j] - dfs(i, j - 1)
            dp[i][j] = max(leftDiff, rightDiff)
            return dp[i][j]
        
        return dfs(0, n - 1) >= 0