# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1]*(amount+1) for i in range(n)]
        def dfs(i,c):
            if memo[i][c] == -1:
                if c == 0 and i < n:
                    memo[i][c] = 1
                elif i == n-1:
                    memo[i][c] = 1 if c%coins[i] == 0 else 0
                else:
                    res = dfs(i+1,c)
                    if c >= coins[i]:
                        res += dfs(i,c-coins[i])
                    memo[i][c] = res
            return memo[i][c]
        return dfs(0,amount)