class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        su = sum(nums)
        pre = 0

        for i in range(n):
            su -= nums[i]
            res = (su - (n-i-1)*nums[i]) + ((i)*nums[i] - pre)
            pre+=nums[i]
            nums[i] = res
        return nums
