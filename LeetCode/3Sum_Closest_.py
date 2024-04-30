class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i,val in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l <r:
                three = val + nums[l] + nums[r]
                if three < target:
                    l+=1
                else:
                    r-=1
                if abs(target - three) < abs(target-closest):
                    closest = three
        return closest
        