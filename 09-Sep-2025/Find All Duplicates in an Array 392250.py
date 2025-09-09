# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i,n = 0,len(nums)
        ans = []
        while i < n:
            if nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        
        for j in range(n):
            if j+1!=nums[j]:
                ans.append(nums[j])
        return ans