class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mi = 1
        ma = max(piles)

        def check(w):
            ho = 0
            for p in piles:
                ho += ceil(p/w)
            return ho

        while mi <= ma:
            mid = mi + (ma-mi)//2
            ho = check(mid)
            if ho > h:
                mi = mid+1
            else:
                ma = mid-1
        return mi