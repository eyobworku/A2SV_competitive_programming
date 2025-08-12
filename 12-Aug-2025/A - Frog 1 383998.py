# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import sys
# import math import  bisect
from collections import defaultdict,deque,Counter
input = lambda:sys.stdin.readline().rstrip()
RI = lambda: int(input())
RII = lambda: map(int, input().split())
RILIST = lambda: list(RII())

# for _ in range(RI()):
n = RI()
a = RILIST()
dp = [0]*n
dp[1]=abs(a[0]-a[1])
for i in range(2,n):
  one = abs(a[i]-a[i-1])
  two = abs(a[i]-a[i-2])
  dp[i] = min(dp[i-1]+one,dp[i-2]+two)
print(dp[n-1])