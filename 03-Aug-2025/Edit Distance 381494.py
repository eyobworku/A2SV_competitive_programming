# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i,j):
            if i >= len(word1) or j >= len(word2):
                if i == len(word1) and j == len(word2):
                    return 0
                elif i == len(word1):
                    return len(word2) - j
                else:
                    return len(word1) - i
            if word1[i] == word2[j]:
                return dp(i+1,j+1) + 0
            else:
                insert = dp(i,j+1) + 1
                delete = dp(i+1,j) + 1
                replace = dp(i+1,j+1) + 1
                return min(insert,delete,replace)
        return dp(0,0)