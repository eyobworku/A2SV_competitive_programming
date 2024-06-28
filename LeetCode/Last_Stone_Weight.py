class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while stones:
            x = -heappop(stones)
            if stones:
                y = -heappop(stones)
                if x>y:
                    heappush(stones,y-x)
                elif y>x:
                    heappush(stones,x-y)
            else:
                return x
        return 0
