# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        arr = [float(0)]*n
        vist = [False] * n
        arr[start_node] = 1.0
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1],succProb[i]))
            graph[edges[i][1]].append((edges[i][0],succProb[i]))

        q = [(-1.0,start_node)]
        heapify(q)
        while q:
            w,nd = heappop(q)
            w*=-1
            if not vist[nd]:
                vist[nd] = True
                for nx,we in graph[nd]:
                    nw_p = w*we
                    if arr[nx] < nw_p:
                        arr[nx] = nw_p
                        heappush(q,(-nw_p,nx))
        return arr[end_node]