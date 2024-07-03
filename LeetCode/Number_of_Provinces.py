class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] *n
        ans = 0
        def dfs(i):
            seen[i] = True
            for j in range(n):
                if isConnected[i][j] and j!=i and not seen[j]:
                    dfs(j)

        for i in range(n):
            if not seen[i]:
                dfs(i)
                ans+=1
        return ans