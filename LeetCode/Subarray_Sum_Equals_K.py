class Solution:        
    def subarraySum(self, nums, k):
        prefix_sum = defaultdict(int)
        maxLength = 0
        currentSum = 0
        prefix_sum[0]=1
        for num in nums:
            currentSum += num
            maxLength += prefix_sum.get(currentSum - k,0)
            prefix_sum[currentSum] += 1
        return maxLength
