# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie  = {}
        for word in wordDict:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = '.'
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(n):
            if not dp[i]:
                continue
            node = trie
            for j in range(i, n):
                if s[j] not in node:
                    break
                node = node[s[j]]
                if '.' in node:
                    dp[j + 1] = True
        return dp[n]