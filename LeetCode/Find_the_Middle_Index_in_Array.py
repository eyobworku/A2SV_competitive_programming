class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sumi = left = 0
        for num in nums:
            sumi += num
        for i in range(len(nums)):
            sumi -= nums[i]
            if left==sumi:
                return i
            left+=nums[i]
        return -1