class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n,res,path=len(candidates),[],[]
        candidates.sort()
        def back(i):
            if sum(path) == target:
                res.append(path[:])
                return
            if i == n or sum(path) > target: return
            
            path.append(candidates[i])
            back(i+1)
            path.pop()
            while i+1 < n and candidates[i] == candidates[i+1]: i+=1

            back(i+1)
            return res
        return back(0)
        