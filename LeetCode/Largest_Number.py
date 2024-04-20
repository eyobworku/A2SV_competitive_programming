class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def custom_sort(x):
            return x * 10
        nums = [str(num) for num in nums]

        nums.sort(key=custom_sort, reverse=True)

        if nums[0] == '0':
            return '0'

        return ''.join(nums)