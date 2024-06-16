class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j,m=0,len(nums)-1,-1
        while i <= j:
            m = (j+i) // 2
            if nums[m]==target:
                break
            if nums[m] > target:
                j=m-1
            else:
                i=m+1
        if m == -1 or nums[m] != target:
            return [-1,-1]
        while m > 0 and nums[m] == nums[m-1]:
            m-=1
        s=m
        while s < len(nums)-1 and nums[s] == nums[s+1]:
            s+=1
        return [m,s]