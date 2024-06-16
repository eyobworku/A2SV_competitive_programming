class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        xlen, ylen, ans, res = len(matrix[0]), len(matrix), 0, defaultdict(int)
        for r in matrix:
            for j in range(1, xlen):
                r[j] += r[j-1]
        
        for j in range(xlen):
            for k in range(j, xlen):
                res.clear()
                res[0], csum = 1, 0
                for i in range(ylen):
                    csum += matrix[i][k] - (matrix[i][j-1] if j else 0)
                    ans += res[csum - target]
                    res[csum] += 1
        return ans