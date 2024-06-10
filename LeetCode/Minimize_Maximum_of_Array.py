class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre = 0
        ans = 0
        for i in range(len(nums)):
            pre+=nums[i]
            ans = max(ans,ceil(pre/(i+1)))
        return ans
