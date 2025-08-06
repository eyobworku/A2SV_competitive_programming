# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = [[0]*(query_row+1) for _ in range(query_row+1)]
        glass[0][0] = poured
        for i in range(query_row):
            for j in range(query_row):
                rm = 0
                if glass[i][j]>=1:
                    rm = glass[i][j]-1
                    glass[i][j]=1
                glass[i+1][j]+=rm/2
                glass[i+1][j+1]+=rm/2
        return min(1,glass[query_row][query_glass])