class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = 0
        for x in nums[:k]:
            sum_+=x
        maxi = sum_/k
        for i,x in enumerate(nums[k:],start=k):
            sum_ -= nums[i-k]
            sum_ +=x
            maxi = max(sum_/k,maxi)
        return maxi

        