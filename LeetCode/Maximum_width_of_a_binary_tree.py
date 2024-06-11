# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque()
        q.append((root,0))
        ma = 0
        while q:
            qlen = len(q)
            _,base = q[0]
            for i in range(qlen):
                node,indx = q.popleft()
                if node.left:
                    q.append((node.left,2*indx))
                if node.right:
                    q.append((node.right,(2*indx)+1))
                ma = max(ma,indx-base+1)
        return ma