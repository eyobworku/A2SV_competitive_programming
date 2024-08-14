class Solution:
    def racecar(self, target: int) -> int:
        turn = 0
        vist = set()
        q = deque([(0,1)])
        vist.add((0,1))
        while q:
            l = len(q)
            for _ in range(l):
                n,s = q.popleft()
                if n == target: return turn
                #forward accelerate
                ap = n+s
                asp = s*2
                if (ap,asp) not in vist:
                    q.append((ap,asp))
                    vist.add((ap,asp))
                #reverse
                rs = -1 if s>0 else 1
                if (n,rs) not in vist:
                    q.append((n,rs))
                    vist.add((n,rs))
            turn+=1