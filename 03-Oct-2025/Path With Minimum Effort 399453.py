# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        heap = [(0,0,0)]
        drx = [(0,1),(1,0),(0,-1),(-1,0)]

        effort = [[float('inf')]*cols for _ in range(rows)]
        effort[0][0] = 0
        while heap:
            cur_w,cr,cc = heappop(heap)
            if cr == rows-1 and cc == cols-1:
                return cur_w
            for dx,dy in drx:
                nx,ny = cr+dx,cc+dy
                if 0<=nx<rows and 0<=ny<cols:
                    new_effort = max(cur_w,abs(
                        heights[cr][cc]-heights[nx][ny]
                    ))
                    if new_effort < effort[nx][ny]:
                        effort[nx][ny]=new_effort
                        heappush(heap,(new_effort,nx,ny))