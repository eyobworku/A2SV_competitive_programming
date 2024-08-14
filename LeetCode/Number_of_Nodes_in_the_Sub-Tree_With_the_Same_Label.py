class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0]*n
        vist = [0]*n
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(i):
            vist[i]=1
            le = [0]*26
            le[ord(labels[i])-97]=1
            for a in graph[i]:
                if vist[a]: continue
                x = dfs(a)
                for j in range(26):
                    le[j]+=x[j]
            ans[i]=le[ord(labels[i])-97]
            return le
        dfs(0)
        return ans