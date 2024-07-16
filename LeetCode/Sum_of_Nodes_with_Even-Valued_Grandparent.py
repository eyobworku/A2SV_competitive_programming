# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(r,gp,pa):
            if not r: return 0
            res = 0
            if gp%2==0: res+=r.val
            return res + dfs(r.left,pa,r.val) + dfs(r.right,pa,r.val)
        return dfs(root,1,1)