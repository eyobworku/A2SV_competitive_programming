# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class UnionFind:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = UnionFind(col*row + 2)
        grid = [[1] * col for _ in range(row)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        cells = [(x-1, y-1) for x, y in cells]

        def index(x, y):
            return x * col + y + 1

        for i in range(len(cells) - 1, -1, -1):
            x, y = cells[i][0], cells[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                ind = index(x+dx, y+dy)
                if x+dx>=0 and x+dx<row and y + dy >= 0 and y + dy < col and grid[x+dx][y+dy]==0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == row - 1:
                dsu.union(col*row + 1, index(x, y))

            if dsu.find(0) == dsu.find(col*row + 1):
                return i