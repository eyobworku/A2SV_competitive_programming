class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]] = 'X'
            return board
        m,n = len(board),len(board[0])
        def isbound(i,j):
            return (0<=i<m) and (0<=j<n)
        drx = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

        def dfs(i,j):
            cnt = 0
            for x,y in drx:
                if isbound(i+x,j+y) and board[i+x][j+y] == 'M':
                    cnt+=1
            if cnt:
                board[i][j] = str(cnt)
            else:
                board[i][j] = 'B'
                for x,y in drx:
                    if isbound(i+x,j+y) and board[i+x][j+y] != 'B':
                        dfs(i+x,j+y)
        dfs(click[0],click[1])
        return board
                    