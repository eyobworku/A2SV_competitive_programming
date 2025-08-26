# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        arr = []
        for i in range(R):
            for j in range(C):
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j]^matrix[i][j-1]^matrix[i-1][j-1]
                elif i:
                    matrix[i][j] ^= matrix[i-1][j]
                elif j:
                    matrix[i][j] ^= matrix[i][j-1]
                arr.append(matrix[i][j])
        arr.sort()
        return arr[-k]