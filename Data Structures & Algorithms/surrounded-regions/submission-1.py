class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        stack = []
        O_list = set()
        visited = set()
        for row in range(ROW):
            for col in range(COL):
                if ((row == 0 or row == ROW -1 or
                    col == 0 or col == COL -1) and 
                    board[row][col] == 'O'):
                    stack.append((row,col))

                if board[row][col] == 'O':
                    O_list.add((row,col))

        def addO(r, c):
            if (min(r,c) < 0 or
                r >= ROW or c >= COL or
                (r,c) in visited or 
                board[r][c] == 'X'):
                return
            stack.append((r,c))


        NEWS = [(1,0), (0,1), (-1,0), (0,-1)]
        while stack:
            row, col = stack.pop()
            visited.add((row,col))
            for dr, dc in NEWS:
                addO(row+dr, col+dc)


        for ro, co in O_list:
            if (ro,co) not in visited:
                board[ro][co] = 'X'


