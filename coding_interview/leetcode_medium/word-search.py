class Solution:
    from collections import deque, Counter
    def exist(self, board: List[List[str]], word: str) -> bool:
        letters = Counter(word)
        options = Counter([x for row in board for x in row])
        if any([x > 0 for x in (letters - options).values()]):
            return False
        stack = deque()
        dirs = ((-1,0), (1,0), (0,-1), (0,1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    stack.append((i,j, deque(dirs)))
                seen = set([(i,j)])
                while stack:
                    if len(stack) == len(word):
                        return True
                    *coord, dirs_left = stack[-1]
                    next_idx = len(stack)
                    while dirs_left:
                        dir = dirs_left.popleft()
                        cell = (coord[0] + dir[0], coord[1] + dir[1])
                        if cell in seen:
                            continue
                        if 0<=cell[0]<len(board) and 0<=cell[1]<len(board[0]) and \
                            board[cell[0]][cell[1]] == word[next_idx]:
                            seen.add(cell)
                            stack.append((*cell, deque(dirs)))
                            break
                    else:
                        x,y,_ = stack.pop()
                        seen.remove((x,y))
        return False