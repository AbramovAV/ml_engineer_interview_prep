class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = list(filter(str.isdigit, board[i]))
            col = list(filter(str.isdigit, [r[i] for r in board]))
            if len(set(row)) < len(row) or len(set(col)) < len(col):
                return False

        for i in range(3):
            for j in range(3):
                sub = [board[x][y] for x in range(3*i, 3*(i+1)) for y in range(3*j, 3*(j+1))]
                sub = list(filter(str.isdigit, sub))
                if len(set(sub)) < len(sub):
                    return False

        return True