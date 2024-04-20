class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        size = nums.count(target)
        index = sorted(nums).index(target)
        return [index+i for i in range(size)]
        