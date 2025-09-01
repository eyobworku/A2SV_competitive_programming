# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        gr = defaultdict(list)
        for x,y,d in roads:
            gr[x].append((y,d))
            gr[y].append((x,d))
        q = deque([(1,float('inf'))])
        vist = set()
        res = float('inf')
        while q:
            a,di = q.popleft()
            res = min(res,di)
            vist.add(a)
            for ch,ds in gr[a]:
                if ch not in vist:
                    q.append((ch,ds))
        return res