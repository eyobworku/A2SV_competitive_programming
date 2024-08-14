class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        m,n = len(board),len(board[0])
        def isbound(i,j):
            return (0<=i<m) and (0<=j<n)
        drx = [(0,1),(-1,0),(1,0),(0,-1)]
        def dfs(i,j):
            board[i][j] = 'W'
            for x,y in drx:
                if isbound(i+x,j+y) and board[i+x][j+y] == 'O':
                    dfs(i+x,j+y)
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'W':
                    board[i][j] = 'O'
