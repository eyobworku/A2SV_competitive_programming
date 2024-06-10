class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxc = [0] * n
        res = 0
        for j in range(n):
            maxi = 0
            for i in range(n):
                maxi = max(maxi,grid[i][j])
            maxc[j] = maxi

        for i in range(n):
            maxr = max(grid[i])
            for j in range(n):
                res += min(maxr,maxc[j])-grid[i][j]

        return res