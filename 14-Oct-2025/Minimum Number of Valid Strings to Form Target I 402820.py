# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self, target):
        self.root = TrieNode()
        self.target = target

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def starts(self, index):
        node = self.root
        l = len(self.target)
        for i in range(index, l):
            if self.target[i] not in node.children:
                return i
            node = node.children[self.target[i]]
        return l


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        t = Trie(target)
        n = len(target)
        for i in words:
            t.insert(i)

        dp = [float("inf")] * (n + 1)
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            index = t.starts(i)
            mn =float("inf")
            for j in range(i, index):
                mn = min(mn, 1 + dp[j + 1])
            dp[i] = mn
        return (dp[0] if dp[0] != float("inf") else -1)