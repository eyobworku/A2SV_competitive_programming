class Solution:
	def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
		temp=sorted(nums)
		return [temp.index(_) for _ in nums]