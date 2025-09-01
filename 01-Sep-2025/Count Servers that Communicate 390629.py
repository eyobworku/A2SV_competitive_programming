# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

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
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dsu = UnionFind(n*m)
        for i in range(n):
            row = []
            for j in range(m):
                if grid[i][j]:
                    row.append(i*m + j)
            if len(row)>1:
                fir = row[0]
                for x in row[1:]:
                    dsu.union(fir,x)
                    fir = x
        for i in range(m):
            col = []
            for j in range(n):
                if grid[j][i]:
                    col.append(j*m + i)
            if len(col)>1:
                fir = col[0]
                for x in col[1:]:
                    dsu.union(fir,x)
                    fir = x
        res = 0
        for i in range(n*m):
            if dsu.size[dsu.find(i)]>1:
                res+=1
        return res