# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        
        memo = {}

        def rec(i, current_):
            if i >= n:
                remain = total - current_
                return abs(remain - current_)
            if (i,current_) not in memo:

                take = rec(i + 1, current_ + stones[i])
                skip = rec(i + 1, current_)

                memo[(i,current_)] = min(take, skip)
            return memo[(i,current_)]

        return rec(0, 0)