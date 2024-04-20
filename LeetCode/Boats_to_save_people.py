class Solution:
    def numRescueBoats(self, arr: List[int], n: int) -> int:
        res = 0
        arr.sort()
        l, r = 0, len(arr) - 1
        while l <= r:
            if arr[l] + arr[r] <= n:
                l += 1
            r -= 1
            res += 1
        return res