class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        nums.sort()
        
        def back(i):
            if i == n:
                res.append(path[:])
                return

            path.append(nums[i])
            back(i+1)

            path.pop()
            while i+1 < n and nums[i] == nums[i+1]: i+=1

            back(i+1)
            return res
        return back(0)