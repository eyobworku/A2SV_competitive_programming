# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys
from collections import defaultdict

def solve():
    n, w = map(int, sys.stdin.readline().split())
    items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    max_value = sum(v for _, v in items)
    
    # dp[i][v] = minimum weight to achieve value v with first i items
    dp = [float('inf')] * (max_value + 1)
    dp[0] = 0  # 0 value requires 0 weight
    
    for weight, value in items:
        # Iterate backwards to avoid overwriting
        for v in range(max_value, value - 1, -1):
            if dp[v - value] + weight < dp[v]:
                dp[v] = dp[v - value] + weight
    
    # Find the maximum v where dp[v] <= w
    result = 0
    for v in range(max_value, -1, -1):
        if dp[v] <= w:
            result = v
            break
    
    print(result)

solve()