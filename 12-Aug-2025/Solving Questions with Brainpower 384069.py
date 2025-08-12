# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, quest: List[List[int]]) -> int:
        n = len(quest)
        memo = [-1] * n
        memo[n-1] = quest[n-1][0]
        
        for i in range(n-2,-1,-1):
            nxt = 0
            if i+quest[i][1]+1<n:
                nxt = memo[i+quest[i][1]+1]
            memo[i] = max(memo[i+1],quest[i][0] + nxt)
        return memo[0]
