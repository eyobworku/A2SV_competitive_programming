class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        res = 0
        right = 0
        for i in range(n):
            right = max(right,flips[i])
            if right == i+1:
                res+=1
        return res
        