class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) -1
        res = 0
        while i < j:
            if nums[i] + nums[j] == k:
                i+=1
                j-=1
                res+=1
            elif nums[i]+ nums[j] < k:
                i+=1
            else:
                j-=1
        return res