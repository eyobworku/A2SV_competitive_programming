# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Node:
    def __init__(self):
        self.isEnd = False
        self.childs = [None] * 26

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Node()
        for word in products:
            node = root
            for l in word:
                idx = ord(l) - ord('a')
                if node.childs[idx] is None:
                    node.childs[idx] = Node()
                node = node.childs[idx]
            node.isEnd = True

        def dfs(node, prefix, res):
            if len(res) == 3:
                return
            if node.isEnd:
                res.append(prefix)
            for i in range(26):
                if node.childs[i]:
                    dfs(node.childs[i], prefix + chr(i + ord('a')), res)
                    if len(res) == 3:
                        return

        ans = []
        node = root
        for i, ch in enumerate(searchWord):
            idx = ord(ch) - ord('a')
            if node and node.childs[idx]:
                node = node.childs[idx]
                res = []
                dfs(node, searchWord[:i+1], res)
                ans.append(res)
            else:
                node = None
                ans.append([])

        return ans
