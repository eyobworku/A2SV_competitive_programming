# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word_end += 1

    def check(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word_end != 0

class Solution:
    def partitionString(self, s: str) -> List[str]:
        trie = Trie()
        word = ''
        segments = []
        for l in s:
            word += l
            if not trie.check(word):
                trie.insert(word)
                segments.append(word)
                word = ''
        return segments