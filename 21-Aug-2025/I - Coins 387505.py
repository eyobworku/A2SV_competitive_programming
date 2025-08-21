# Problem: I - Coins - https://atcoder.jp/contests/dp/tasks/dp_i

import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(float, input().split())
RILIST = lambda: list(RII())

N = RI()
ps = RILIST()
dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1.0

for i in range(1, N + 1):
    p = ps[i - 1]
    for j in range(i + 1):
        dp[i][j] = dp[i - 1][j] * (1 - p)
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * p

ans = sum(dp[N][j] for j in range((N // 2) + 1, N + 1))
print(ans)