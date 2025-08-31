# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))
        
        def dfs(src, dst, visited,prod=1):
            if src == dst: return prod
            visited.add(src)
            for nei, val in graph[src]:
                if nei not in visited:
                    result = dfs(nei, dst, visited, prod * val)
                    if result != -1.0: return result
            return -1.0

        results = []
        for u, v in queries:
            if u not in graph or v not in graph: results.append(-1.0) ; continue
            else:
                visited = set()
                results.append(dfs(u, v,visited))
        
        return results