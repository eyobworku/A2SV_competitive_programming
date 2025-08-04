# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[-1]*(amount+1) for i in range(n)]
        def dfs(i,c):
            if i == 0:
                if c%coins[i] == 0:
                    return c//coins[i]
                return 1e9
            if memo[i][c] == -1:
                exclude = dfs(i-1,c)
                include = 1e9
                if c >= coins[i]:
                    include = 1 + dfs(i,c-coins[i])
                memo[i][c] = min(include,exclude)
            return memo[i][c]
        res = dfs(n-1,amount)
        return -1 if res >= 1e9 else res