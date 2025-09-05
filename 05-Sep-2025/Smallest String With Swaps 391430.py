# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

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
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind(len(s))

        for x,y in pairs:
            dsu.union(x,y)
        
        letters = defaultdict(list)
        for i in range(len(s)):
            rep = dsu.find(i)
            letters[rep].append(s[i])
        
        for letter in letters:
            letters[letter].sort(reverse = True)
        
        res = ""

        for i in range(len(s)):
            rep = dsu.find(i)
            res += letters[rep].pop()
        
        return res