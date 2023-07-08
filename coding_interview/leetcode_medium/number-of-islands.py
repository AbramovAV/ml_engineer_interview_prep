class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        dirs = ((-1, 0), (0, -1), (1,0), (0,1))
        land_queue = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    land_queue.append((i,j))
                    while land_queue:
                        x,y = land_queue.pop()
                        grid[x][y] = -1
                        for dir in dirs:
                            adj_x, adj_y = x+dir[0], y+dir[1]
                            if 0<=adj_x<rows and \
                                0<=adj_y<cols and \
                                grid[adj_x][adj_y]=="1":
                                land_queue.append((adj_x, adj_y))
                    counter += 1
        return counter