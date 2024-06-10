# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root,i):
            if not root: return
            if len(res) < i+1:
                res.append(deque())
            if i%2:
                res[i].appendleft(root.val)
            else:
                res[i].append(root.val)
            bfs(root.left,i+1)
            bfs(root.right,i+1)
        bfs(root,0)
        return res