class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0]=1
        curr = total = 0
        
        for n in nums:
            curr += n
            total+=count[curr-goal] 
            count[curr]+=1

        return total