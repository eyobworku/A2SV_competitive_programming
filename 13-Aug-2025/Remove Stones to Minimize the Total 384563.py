# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)
        while k > 0:
            k-=1
            a = heappop(piles)
            a//=2
            heappush(piles,a)
        return -sum(piles)