class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_de , d_de = deque(),deque()
        n = len(senate)

        for i in range(n):
            if senate[i]=='R':
                r_de.append(i)
            else:
                d_de.append(i)

        while r_de and d_de:
            r = r_de.popleft()
            d = d_de.popleft()
            if r < d:
                r_de.append(r+n)
            else:
                d_de.append(d+n)

        return 'Radiant' if r_de else 'Dire'
        