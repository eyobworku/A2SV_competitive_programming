# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = deque()
        Q.append((root,0))
        res = defaultdict(list)
        n = 0
        while Q:
            nod,l = Q.popleft()
            res[l].append(nod.val)
            n = max(n,l)
            if nod.left:
                Q.append((nod.left,l+1))
            if nod.right:
                Q.append((nod.right,l+1))
        ans = []
        for i in range(n+1):
            ans.append(sum(res[i])/len(res[i]))
        return ans