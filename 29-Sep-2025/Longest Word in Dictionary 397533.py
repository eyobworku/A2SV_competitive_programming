# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Node:
    def __init__(self):
        self.isEnd = False
        self.childs = [None] * 26
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Node()
        for word in words:
            node = root
            for l in word:
                idx = ord(l)-97
                if node.childs[idx] is None:
                    node.childs[idx] = Node()
                node = node.childs[idx]
            node.isEnd = True
            
        def find(word):
            node = root
            for ch in range(len(word) - 1):
                inx = ord(word[ch])-97
                if node.childs[inx] == None:
                    return False
                node = node.childs[inx]
                if not node.isEnd:
                    return False
            return True

        res = ""
        for i in sorted(words):
            if find(i):
                if len(i) > len(res):
                    res = i
        return res