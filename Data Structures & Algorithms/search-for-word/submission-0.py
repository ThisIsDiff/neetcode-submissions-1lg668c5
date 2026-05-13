class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x_max = len(board[0])
        y_max = len(board)
        ls = set()

        def dfs(x, y, w):
            if w =="":
                return True 
            if (x < 0 or y < 0 or 
                y >= y_max or x >= x_max or 
                board[y][x] != w[0] or 
                (x, y) in ls) :
                return False

            ls.add((x, y))



            res =  (
                dfs(x + 1, y,  w[1:]) or 
                dfs(x - 1, y,  w[1:]) or 
                dfs(x, y + 1,  w[1:]) or 
                dfs(x, y - 1,  w[1:]))

            ls.remove((x, y))
            return res

        res = False
        for len_y in range(y_max):
            for len_x in range(x_max):
                if dfs(len_x, len_y, word):
                    return True
            

        return False