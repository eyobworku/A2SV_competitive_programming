# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.val = 0

class MapSum:

    def __init__(self):
        self.hashmap = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self.hashmap[key] = val
        node = self.root
        for l in key:
            if node.children[ord(l) - ord('a')] == None:
                node.children[ord(l) - ord('a')] = TrieNode()
            node = node.children[ord(l) - ord('a')]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for l in prefix:
            if node.children[ord(l) - ord('a')] == None:
                return 0
            node = node.children[ord(l) - ord('a')]
        
        summ = [0]
        def recursivelyCheck(node):
            summ[0] += node.val
            for n in node.children:
                if n:
                    recursivelyCheck(n)
                    
        recursivelyCheck(node)
        return summ[0]
        



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)