# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.next:
                node.next[char] = TrieNode()
            node = node.next[char]
        node.is_end = True

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.dp = []
        self.n = 0

    def dfs(self, s: str, start: int) -> list:
        if start == self.n:
            return [""]
        if self.dp[start]:
            return self.dp[start]

        ans = []
        node = self.trie.root
        current_prefix = ""

        for i in range(start, self.n):
            char = s[i]
            if char not in node.next:
                break

            node = node.next[char]
            current_prefix += char

            if node.is_end:
                rest = self.dfs(s, i + 1)
                for r in rest:
                    ans.append(current_prefix + (" " + r if r else ""))

        self.dp[start] = ans
        return self.dp[start]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.n = len(s)
        self.dp = [[] for _ in range(self.n + 1)]
        
        for word in wordDict:
            self.trie.insert(word)

        return self.dfs(s, 0)