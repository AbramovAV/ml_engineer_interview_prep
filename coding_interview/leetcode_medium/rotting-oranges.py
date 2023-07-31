class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter = 0
        rotten = set()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i,j))
        going_to_rot = set()
        dirs = ((-1,0), (0,-1), (1,0), (0,1))
        while fresh:
            for orange in fresh:
                if any([(orange[0]+i, orange[1]+j) in rotten for (i,j) in dirs]):
                    going_to_rot.add(orange)
            if not going_to_rot:
                return -1
            else:
                fresh -= going_to_rot
                rotten |= going_to_rot
                going_to_rot = set()
                counter += 1
        return counter