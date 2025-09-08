# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma:
            return 0
        bucketSize = math.ceil((ma - mi) / (n - 1))
        minBucket = [math.inf] * n
        maxBucket = [-math.inf] * n
        for x in nums:
            idx = (x - mi) // bucketSize
            minBucket[idx] = min(minBucket[idx], x)
            maxBucket[idx] = max(maxBucket[idx], x)

        maxGap = bucketSize
        prev = maxBucket[0]
        for i in range(1, n):
            if minBucket[i] == math.inf:
                continue
            maxGap = max(maxGap, minBucket[i] - prev)
            prev = maxBucket[i]
        return maxGap