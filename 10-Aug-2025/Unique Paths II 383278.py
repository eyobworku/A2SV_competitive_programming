# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def inbound(i,j):
            if (0 <= i < m and 0 <= j < n):
                return grid[i][j]
            return True
        memo = {}
        def dp(i,j):
            if inbound(i,j):
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            paths = 0
            paths += dp(i+1,j) 
            paths += dp(i,j+1)
            memo[(i,j)] = paths
            return paths
        return dp(0,0)