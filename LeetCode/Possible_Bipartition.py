class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a,b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        col = [-1]*n
        ans = True
        def dfs(node):
            nonlocal ans
            for n in graph[node]:
                if col[n] == col[node]:
                    ans=False
                else:
                    if col[n] == -1:
                        col[n] = col[node]^1
                        dfs(n)       
            return
        for i in range(n):
            if col[i] == -1:
                col[i]=0
                dfs(i)
        return ans