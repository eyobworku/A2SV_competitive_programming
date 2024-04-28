class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        secondVal = float('-inf')
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < secondVal:
                return True
            while stack and stack[-1] < nums[i]:
                secondVal = stack.pop()
            stack.append(nums[i])
        
        return False
