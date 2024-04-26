class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [[0]*n for _ in range(m)]
        for i,j in walls+guards:
            arr[i][j]=1

        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for x, y in guards:
            for dx, dy in dir:
                curr_x = x
                curr_y = y
                
                while 0 <= curr_x+dx < m and 0 <= curr_y+dy < n and arr[curr_x+dx][curr_y+dy] != 1:
                    curr_x += dx
                    curr_y += dy
                    arr[curr_x][curr_y] = 2
                    
        return sum(1 for i in range(m) for j in range(n) if arr[i][j] == 0)