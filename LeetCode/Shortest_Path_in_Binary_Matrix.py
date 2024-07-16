class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)-1
        if grid[0][0] or grid[n][n]: return -1
        if len(grid) == 1: return 1
        q = deque([(1,0,0)])
        drx = [(1,1),(-1,0),(-1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        while q:
            for _ in range(len(q)):
                l,x,y = q.popleft()
                for i,j in drx:
                    nx = x+i;ny=y+j
                    if nx < 0 or nx>n or ny < 0 or ny>n or grid[nx][ny]:
                        continue
                    if nx == n and ny == n: return l+1
                    grid[nx][ny] = 2
                    q.append((l+1,nx,ny))
        return -1