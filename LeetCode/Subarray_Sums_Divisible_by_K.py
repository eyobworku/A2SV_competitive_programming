class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remind = collections.defaultdict(int)
        remind[0] = 1
        cnt = runing = 0
        for num in nums:
            runing+=num

            if runing % k in remind:
                cnt+=remind[runing % k]
            
            remind[runing % k]+=1
        return cnt

