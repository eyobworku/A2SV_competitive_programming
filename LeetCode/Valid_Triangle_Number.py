class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            l,h=0,i-1
            while l < h:
                if nums[l]+nums[h]>nums[i]:
                    count+=(h-l)
                    h-=1
                else:
                    l+=1
        return count