"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #nonlocal res
        if not root:
            return 0
        def dfs(node, ma):
            if not node.children:
                return ma
            return max(dfs(child, ma + 1) for child in node.children)
        return dfs(root, 1)