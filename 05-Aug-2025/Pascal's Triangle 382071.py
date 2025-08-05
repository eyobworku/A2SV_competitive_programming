# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2,numRows+1):
            ar = [1]
            for j in range(1,i-1):
                ar.append(res[-1][j]+res[-1][j-1])
            ar.append(1)
            res.append(ar)
        return res