class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        sumi = 0
        j = 0
        for i in range(len(nums)):
            if dic[nums[i]] != 0:
                while dic[nums[i]] != 0:
                    sumi-=nums[j]
                    dic[nums[j]]-=1
                    j+=1
            sumi+=nums[i]
            dic[nums[i]]+=1
            ans = max(ans,sumi)
        return ans