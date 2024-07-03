# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            if not root: return ''
            res = str(root.val)
            l = dfs(root.left)
            r = dfs(root.right)
            if l == '' and r == '': return res
            elif r == '': return f'{res}({l})'
            else: return f'{res}({l})({r})' #  res+'('+l+')'+'('+r+')'
        return dfs(root)