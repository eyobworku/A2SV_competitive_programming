# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges)+1)
        res = []
        for x,y in edges:
            xp = dsu.find(x)
            yp = dsu.find(y)
            if xp == yp:
                res = [x,y]
            else:
                dsu.union(x,y)
        return res