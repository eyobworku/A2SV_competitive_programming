# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = []
        def dfs(root,path):
            if not root: return
            if not root.left and not root.right:
                path+=str(root.val)
                val.append(int(path))
            else:
                dfs(root.left,path+str(root.val))
                dfs(root.right,path+str(root.val))
        dfs(root,'')
        return sum(val)