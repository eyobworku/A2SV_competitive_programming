class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0]*n
        out[0]=1
        for i in range(1,n):
            out[i] = out[i-1]*nums[i-1]
        right =1
        for i in range(n-1,-1,-1):
            out[i] *= right
            right *= nums[i]
        return out