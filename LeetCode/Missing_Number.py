class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,n = 0,len(nums)
        while i < n:
            if nums[i] < n and nums[i] != i:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
            else:
                i+=1
        
        for j in range(n):
            if j!=nums[j]:
                return j
        return n
        