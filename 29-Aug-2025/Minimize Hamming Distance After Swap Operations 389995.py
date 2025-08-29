# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

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
        if parX != parY:
            if self.rank[parX] > self.rank[parY]:
                self.root[parY] = parX
            elif self.rank[parX] < self.rank[parY]:
                self.root[parX] = parY
            else:
                self.root[parX] = parY
                self.rank[parY]+=1
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = UnionFind(n)
        for x,y in allowedSwaps:
            dsu.union(x,y)
        res = 0
        group = defaultdict(list)
        for i in range(n):
            group[dsu.find(i)].append(i)
        for i,items in group.items():
            cntt = defaultdict(int)
            cnts = defaultdict(int)
            elem = set()
            for inx in items:
                cnts[source[inx]]+=1
                cntt[target[inx]]+=1
                elem.add(source[inx])
                elem.add(target[inx])
            for x in elem:
                res+=abs(cntt[x]-cnts[x])
        return res//2
