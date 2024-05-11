class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        tota=0
        res=len(nums)+1
        for i in range(len(nums)):
            tota+=nums[i]
            if tota >= target:
                while (tota - nums[j]) >=target:
                    tota-=nums[j]
                    j+=1
                res = min(res,i-j+1)
        return 0 if res > len(nums) else res


        