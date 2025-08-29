# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = UnionFind(n)
        res = []

        for i in range(len(requests)):
            f,s = dsu.find(requests[i][0]),dsu.find(requests[i][1])
            can = True
            for a, b in restrictions:
                pa, pb = dsu.find(a), dsu.find(b)
                if (pa == f and pb == s) or (pa == s and pb == f):
                    can = False
                    break
            if can:
                dsu.union(f, s)
            res.append(can)
        return res
        