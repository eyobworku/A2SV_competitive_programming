class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for i0 in range(m//2):
            i1 = m-i0-1
            for j0 in range(i0, i1):
                j1 = m-j0-1
                
                matrix[j0][i1],matrix[i1][j1],matrix[j1][i0],matrix[i0][j0] = matrix[i0][j0],matrix[j0][i1],matrix[i1][j1],matrix[j1][i0]
