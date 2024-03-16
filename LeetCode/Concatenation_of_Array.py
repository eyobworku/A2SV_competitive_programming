from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n,2*n):
            nums.append(nums[i-n])
        return nums