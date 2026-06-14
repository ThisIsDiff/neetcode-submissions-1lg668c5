from collections import deque 
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        TREASURE = 0
        WATER = -1
        LAND = 2147483647
        ROW, COL = len(grid), len(grid[0])
        q = deque()        
        visited = set()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == TREASURE:
                    q.append((row,col))
                    visited.add((row,col))


        def addCell(r, c):
            if (min(r,c) < 0 or
                r == ROW or
                c == COL or 
                (r,c) in visited or 
                grid[r][c] == WATER):
                return
            q.append((r,c))
            visited.add((r,c))



        NEWS = [(1,0), (0,1), (-1,0),  (0,-1)]
        dist = 0

        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist
                for direction in NEWS:
                    addCell(direction[0] + r, direction[1] + c)
            dist += 1



