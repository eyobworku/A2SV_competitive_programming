class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0]*n
        adj = [[0]*n for _ in range(n)]
        res = 0
        for x,y in roads:
            deg[x]+=1
            deg[y]+=1
            adj[x][y] = 1
            adj[y][x] = 1
        
        for i in range(n-1):
            for j in range(i+1,n):
                res = max(res,deg[i]+deg[j]-adj[i][j])

        return res