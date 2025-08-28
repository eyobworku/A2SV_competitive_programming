# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parn = [i for i in range(26)]
        rank = [1] * 26

        def find(x):
            while x != parn[x]:
                parn[x] = parn[parn[x]]
                x = parn[x]
            return x

        def union(x,y):
            parX = find(x);parY = find(y)
            if parX != parY:
                if rank[parX] > rank[parY]:
                    parn[parY] = parX
                elif rank[parX] < rank[parY]:
                    parn[parX] = parY
                else:
                    parn[parX] = parY
                    rank[parY]+=1
        for e in equations:
            f,s = ord(e[0])-97,ord(e[3])-97
            if e[1] == '=':
                union(f,s)
        for e in equations:
            f,s = ord(e[0])-97,ord(e[3])-97
            if e[1] == '!':
                if find(f) == find(s): return False

        return True