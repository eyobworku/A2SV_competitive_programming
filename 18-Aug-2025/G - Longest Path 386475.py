# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

N, M = RII()
graph = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    x, y = RII()
    x -= 1
    y -= 1
    graph[x].append(y)
    indegree[y] += 1

q = deque([i for i in range(N) if indegree[i] == 0])
dp = [0] * N  

while q:
    u = q.popleft()
    for v in graph[u]:
        if dp[v] < dp[u] + 1:
            dp[v] = dp[u] + 1
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print(max(dp))