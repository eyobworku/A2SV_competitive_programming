# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())
MOD = 10**9 + 7

h,w = RII()
mat = []
for _ in range(h):
  mat.append(list(input()))
  
dp = [[0]*w for _ in range(h)]

dp[0][0]=1

for i in range(h):
  for j in range(w):
    if mat[i][j]=='#':
      dp[i][j]=0
    else:
      dp[i][j] += (dp[i-1][j] if i-1 >= 0 else 0) + (dp[i][j-1] if j-1 >= 0 else 0)
      dp[i][j] %= MOD

print(dp[-1][-1]%MOD)