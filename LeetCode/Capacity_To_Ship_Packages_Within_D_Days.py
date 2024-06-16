class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_w = max(weights)
        max_w = sum(weights)
        def check(w):
            d = 1
            run = 0
            for we in weights:
                if run+we <= w:
                    run+=we
                else:
                    d+=1
                    run = we
            return d
        while min_w <= max_w:
            mid = min_w + (max_w - min_w) // 2
            d = check(mid)
            if d > days:
                min_w = mid+1
            else:
                max_w = mid-1
        
        return min_w