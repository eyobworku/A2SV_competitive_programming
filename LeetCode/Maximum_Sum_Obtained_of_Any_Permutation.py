class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        req = [0]*(n+1)
        for x in requests:
            req[x[0]]+=1
            req[x[1]+1]-=1
        req = list(accumulate(req))
        req.pop()
        req.sort()
        nums.sort()
        return sum(req[i]*nums[i] for i in range(n))%1000000007
        