from collections import deque 
class Solution:
    TREASURE = 0
    WATER = -1
    LAND = 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        mostRecentTreasure = None
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == self.LAND:
                    grid[row][col] = self.bfs(grid, row, col)


    def bfs(self,grid,row, col):
        q = deque([[row,col,0]])
        NEWS = [(1,0), (0,1), (-1,0),  (0,-1)]
        visited = set()
        while q:
            r, c, distance = q.popleft()
            visited.add((r,c))

            if grid[r][c] == self.TREASURE:
                return distance

            for direction in NEWS:
                dr = direction[0] + r
                dc = direction[1] + c


                if (0 <= dr < len(grid) and
                    0 <= dc < len(grid[0]) and
                    (dr,dc) not in visited and 
                    grid[dr][dc] != self.WATER):
                    q.append((dr,dc, distance + 1))

        return self.LAND


