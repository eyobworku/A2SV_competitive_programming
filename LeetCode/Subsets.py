class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        
        def backtrack(i):
            if i==n:
                res.append(path.copy())
                return

            next_num = nums[i]

            #don't use number
            backtrack(i+1)

            #use number
            path.append(next_num)
            backtrack(i+1)
            path.pop()
            return res
        
        return backtrack(0)