class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i , n = 0, len(nums)
        while i < n:
            if nums[i] > n or nums[i] < 1: i+=1
            elif nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1