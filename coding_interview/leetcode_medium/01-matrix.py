class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        dirs = ((-1,0), (0,-1), (1,0), (0,1))
        for i in range(rows):
            for j in range(cols):
                if not mat[i][j]:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1

        while queue:
            x,y = queue.popleft()
            for dir in dirs:
                xx,yy = x+dir[0], y+dir[1]
                if 0<=xx<rows and 0<=yy<cols and mat[xx][yy] == -1:
                    mat[xx][yy] = mat[x][y]+1
                    queue.append((xx,yy))
        return mat