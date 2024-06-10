# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,mi,ma):
            global res
            if not root: return
            self.res = max(self.res,abs(root.val-mi),abs(root.val-ma))
            dfs(root.left,min(root.val,mi),max(root.val,ma))
            dfs(root.right,min(root.val,mi),max(root.val,ma))
        dfs(root,root.val,root.val)
        return self.res