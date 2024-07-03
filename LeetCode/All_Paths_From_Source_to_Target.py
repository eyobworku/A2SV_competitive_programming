class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        res = []
        
        def dfs(v,path):
            path.append(v)
            if v == n:
                res.append(path)
                return
            for i in graph[v]:
                dfs(i,path.copy())
        dfs(0,[])
        return res
