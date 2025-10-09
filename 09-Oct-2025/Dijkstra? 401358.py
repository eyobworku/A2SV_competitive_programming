# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import sys
# import math
# import  bisect
from collections import defaultdict,deque,Counter
from heapq import heappop,heappush,heapify
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

n,m=RII()
res = []
graph = defaultdict(list)
for _ in range(m):
    s,d,t = RII()
    graph[d].append((s,t))
    graph[s].append((d,t))

dist = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)

dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            parent[v] = u
            heappush(pq, (dist[v], v))

if dist[n] == float('inf'):
    print(-1)
else:
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*path[::-1])