class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        ans=0
        print(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                print(i)
                ans+=i
        return ans         