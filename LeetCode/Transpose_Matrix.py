class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                res[x][y]=matrix[y][x]
        return res