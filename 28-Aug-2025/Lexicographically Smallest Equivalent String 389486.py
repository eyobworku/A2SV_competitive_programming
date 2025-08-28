# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = UnionFind(26)
        n = len(s1)
        for i in range(n):
            dsu.union(ord(s1[i])-97,ord(s2[i])-97)
        res = ''
        for x in baseStr:
            res+=chr(dsu.find(ord(x)-97)+97)
        return res        