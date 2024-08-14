class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m = len(maze),len(maze[0])
        drx = [(1,0),(0,1),(-1,0),(0,-1)]
        def isbound(i,j):
            return (0<=i<n) and (0<=j<m)
        q = deque([(entrance[0],entrance[1])])
        maze[entrance[0]][entrance[1]] = '+'
        entrance = tuple(entrance)
        turn = 1
        while q:
            l = len(q)
            for _ in range(l):
                i,j = q.popleft()
                for x,y in drx:
                    nx,ny = i+x,j+y
                    if isbound(nx,ny) and maze[nx][ny] == '.':
                        if (nx,ny) != entrance and (nx==0 or nx==n-1 or ny==0 or ny==m-1):
                            return turn
                        else:
                            maze[nx][ny] = '+'
                            q.append((nx,ny))
            turn+=1
        return -1