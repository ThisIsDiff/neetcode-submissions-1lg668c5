class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # #row check
        # for row in board:
        #     counter = [0]*9
        #     for num in row:
        #         if num == '.':
        #             continue 
        #         counter[int(num) -1] += 1
        #     for c in counter:
        #         if c > 1:
        #             return False

        # #col check
        # for colnum in range(9):
        #     counter = [0] * 9
        #     for rownum in range(9):
        #         val = board[rownum][colnum]
        #         if val == '.':
        #             continue
        #         counter[int(val) - 1] += 1
        #     for c in counter:
        #         if c > 1:
        #             return False

        # #3x3 check
        # squareCollection = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]

        # for row, col in squareCollection:
        #     counter = [0] * 9
        #     for r in range(row-1, row + 2):
        #         for c in range(col-1, col + 2):
        #             val = board[r][c]
        #             if val == '.':
        #                 continue
        #             counter[int(val) - 1] += 1
        #             for c in counter:
        #                 if c > 1:
        #                     return False

        # return True

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True

        