class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        ans= 0
        for i,v in enumerate(tickets):
            q.append([i,v])

        while q:
            i,v = q.popleft()
            v -=1
            ans +=1
            if v != 0:
                q.append((i,v))
            if i == k and v == 0:
                return ans
        return ans
             