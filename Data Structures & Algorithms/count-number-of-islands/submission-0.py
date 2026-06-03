from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        news = [[1,0], [-1,0], [0,1], [0,-1]]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                q = deque()
                if grid[row][col] == "1":
                    q.append([row,col])
                    while q:
                        qr, qc = q.popleft()
                        grid[qr][qc] = "0"
                        for dir_row, dir_col in news:
                            new_row = qr + dir_row
                            new_col = qc + dir_col
                            if  ((0<= new_row < len(grid)) and (0<= new_col < len(grid[0])) and (grid[new_row][new_col] == "1")):
                                q.append((new_row,new_col))    
                    islands +=1

        return islands
