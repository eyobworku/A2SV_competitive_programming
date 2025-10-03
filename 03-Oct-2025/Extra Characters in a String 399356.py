# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class Node:
    def __init__(self):
        self.isEnd = False
        self.childs = {}
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Node()
        for word in dictionary:
            node = root
            for l in word:
                if l not in node.childs:
                    node.childs[l] = Node()
                node = node.childs[l]
            node.isEnd = True

        dp = {len(s):0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i+1)
            curr = root
            for j in range(i,len(s)):
                if s[j] not in curr.childs:
                    break
                curr = curr.childs[s[j]]
                if curr.isEnd:
                    res = min(res,dfs(j+1))
            dp[i]=res
            return res
        return dfs(0)
