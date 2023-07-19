class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.coords = set()
        self.dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])
        self.heights = heights
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.hit_pacific = False
                self.hit_atlantic = False
                self.seen = set()
                self.dfs(i,j)
                if self.hit_pacific and self.hit_atlantic:
                    self.coords.add((i,j))
        return list(self.coords)

    def dfs(self, row, col):
        if self.hit_pacific and self.hit_atlantic:
            return
        self.seen.add((row, col))
        for dir in self.dirs:
            roww, coll = row+dir[0], col+dir[1]
            if (roww, coll) in self.seen:
                continue
            if 0 <= roww < self.num_rows and 0 <= coll < self.num_cols:
                if self.heights[roww][coll] <= self.heights[row][col]:
                    if (roww, coll) in self.coords:
                        self.hit_pacific = True
                        self.hit_atlantic = True
                    self.dfs(roww, coll)
            elif roww < 0 or coll < 0:
                self.hit_pacific = True
            elif roww >= self.num_rows or coll >= self.num_cols:
                self.hit_atlantic = True