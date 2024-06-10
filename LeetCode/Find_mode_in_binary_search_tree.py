# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not root.left and not root.right:
            return [root.val]

        dic = defaultdict(int)
        def help(root):
            dic[root.val] += 1
            if not root.left and not root.right:
                return 
            if root.left:
                help(root.left)
            if root.right:
                help(root.right)
        help(root)
        res = []
        ma = max(dic.values())
        for key, value in dic.items():
            if value == ma:
                res.append(key)
        return res
        