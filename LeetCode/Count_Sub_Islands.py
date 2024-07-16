class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1),len(grid1[0])
        res = 0

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or not grid2[i][j]: return
            grid2[i][j] = 0
            dfs(i+1,j);dfs(i,j+1);dfs(i-1,j);dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] and not grid1[i][j]:
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    dfs(i,j)
                    res+=1
        return res