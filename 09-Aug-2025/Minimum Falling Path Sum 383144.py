# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        for i in range(1,n):
            for j in range(m):
                val = matrix[i-1][j]
                if j>0:
                    val = min(val,matrix[i-1][j-1])
                if j<m-1:
                    val = min(val,matrix[i-1][j+1])
                matrix[i][j]+=val
        return min(matrix[n-1])