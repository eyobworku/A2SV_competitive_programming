# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys
# import math import  bisect
from collections import defaultdict,deque,Counter
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

n,k = RII()
a = RILIST()
dp = [float('inf')] * n
dp[0] = 0  

for i in range(n-1):
  for j in range(1, k + 1):
    if i + j > n-1:
      break

    dp[i+j] = min(dp[i+j], dp[i] + abs(a[i] - a[i+j]))
print(dp[n-1])