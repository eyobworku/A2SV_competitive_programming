# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = UnionFind(n*m)
        island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    island+=1
                    for ir, ic in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nr, nc = i + ir, j + ic
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                            if dsu.find(i*m+j)!=dsu.find(nr*m+nc):
                                island-=1
                                dsu.union(i*m+j,nr*m+nc)
        opens = set()
        for i in range(n):
            if grid[i][0]==0:
                opens.add(dsu.find(i*m))
            if grid[i][m-1]==0:
                opens.add(dsu.find(i*m + m-1))
        for i in range(m):
            if grid[0][i]==0:
                opens.add(dsu.find(i))
            if grid[n-1][i]==0:
                opens.add(dsu.find((n-1)*m + i))
        return island - len(opens)
