class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(arr,i):
            if len(arr) == k:
                res.append(arr)
                return
            for j in range(i+1,n+1):
                dfs(arr+[j],j)
        dfs([],0)
        return res