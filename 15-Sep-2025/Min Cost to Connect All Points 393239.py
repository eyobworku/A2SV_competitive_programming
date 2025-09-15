# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    def union(self, x, y):
        parX = self.find(x);parY = self.find(y)
        if parX == parY:
            return False
        if self.rank[parX] > self.rank[parY]:
            self.root[parY] = parX
        elif self.rank[parX] < self.rank[parY]:
            self.root[parX] = parY
        else:
            self.root[parX] = parY
            self.rank[parY]+=1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (dist, i, j))

        dsu = UnionFind(n)
        cost, edges_used = 0, 0

        while edges_used != (n- 1):
            dist,u,v= heapq.heappop(edges)
            if dsu.union(u, v):
                cost += dist
                edges_used += 1

        return cost