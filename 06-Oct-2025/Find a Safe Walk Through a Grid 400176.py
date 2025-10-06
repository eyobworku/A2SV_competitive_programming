# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows,cols = len(grid),len(grid[0])
        drx = [(0,1),(1,0),(0,-1),(-1,0)]

        effort = [[float('inf')]*cols for _ in range(rows)]
        effort[0][0] = -health + grid[0][0]
        heap = [(effort[0][0],0,0)]

        while heap:
            cur_w,cr,cc = heappop(heap)
            for dx,dy in drx:
                nx,ny = cr+dx,cc+dy
                if 0<=nx<rows and 0<=ny<cols:
                    if cur_w + grid[nx][ny] < effort[nx][ny]:
                        effort[nx][ny]=cur_w + grid[nx][ny]
                        heappush(heap,(cur_w + grid[nx][ny],nx,ny))
        return effort[rows-1][cols-1] < 0