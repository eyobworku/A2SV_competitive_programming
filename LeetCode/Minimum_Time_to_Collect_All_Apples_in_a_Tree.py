class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visted = [0] * n
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(i):
            res = 0
            visted[i] = 1
            for x in graph[i]:
                if visted[x]: continue
                res += dfs(x)
                
            if i>0 and (hasApple[i] or res > 0):
                res+=2
            return res
        return dfs(0)