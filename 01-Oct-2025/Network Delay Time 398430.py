# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n , k: int) -> int:
        arr = [float('inf')]*n
        k-=1
        arr[k] = 0
        graph = defaultdict(list)
        for s,d,t in times:
            graph[s-1].append((d-1,t))

        q = [(k,0)]
        heapify(q)
        while q:
            nd,w = heappop(q)
            for nx,we in graph[nd]:
                if arr[nx] > arr[nd] + we:
                    arr[nx] = arr[nd] + we
                    heappush(q,(nx,arr[nx]))
        res = max(arr)
        return -1 if res==float('inf') else res