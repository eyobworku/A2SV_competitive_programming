class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        res = 1
        for x in range(1,mn+1):
            if mn%x == 0 and mx%x == 0:
                res =x
        return res
