class Solution:
    from collections import deque
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        coords = set()
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        num_rows = len(heights)
        num_cols = len(heights[0])
        for i in range(num_rows):
            for j in range(num_cols):
                hit_pacific = False
                hit_atlantic = False
                queue = deque([(i,j)])
                seen = set()
                while queue:
                    if hit_pacific and hit_atlantic:
                        break
                    row,col = queue.popleft()
                    seen.add((row, col))
                    for dir in dirs:
                        roww, coll = row+dir[0], col+dir[1]
                        if (roww, coll) in seen:
                            continue
                        if 0 <= roww < num_rows and 0 <= coll < num_cols:
                            if heights[roww][coll] <= heights[row][col]:
                                if (roww, coll) in coords:
                                    hit_pacific = True
                                    hit_atlantic = True
                                queue.append((roww, coll))
                        elif roww < 0 or coll < 0:
                            hit_pacific = True
                        elif roww >= num_rows or coll >= num_cols:
                            hit_atlantic = True
                if hit_pacific and hit_atlantic:
                    coords.add((i,j))
        return list(coords)