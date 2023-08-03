class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        time = 0

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 2 :
                    q.append((i,j,0))
                    visited[i][j] = True


        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]

        while q : 
           
            i , j , time = q.pop(0)
            
            for c in range(4):
                nrow = i + drow[c]
                ncol = j + dcol[c]

                if 0<= nrow < row and 0<= ncol < col and not visited[nrow][ncol] and grid[nrow][ncol] == 1 :
                    q.append((nrow,ncol,time+1))
                    visited[nrow][ncol] = True
                    grid[nrow][ncol] = 2


        for i in range(row):
            for j in range(col):

                if grid[i][j] == 1 :
                    return -1
        
        return time
            

            

        