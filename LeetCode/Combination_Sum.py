class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(candidates)

        def back(i):
            if target == sum(sol):
                res.append(sol[:])
                return
            if i == n or sum(sol) > target:
                return

            back(i+1)

            sol.append(candidates[i])
            back(i)
            sol.pop()
            return res
        return back(0)
