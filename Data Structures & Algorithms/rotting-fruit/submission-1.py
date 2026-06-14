from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        ROW, COL = len(grid), len(grid[0])
        banana_count = 0
        fresh_count = 0
        q = deque()
        visited = set()
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == ROTTEN:
                    q.append((row,col))
                    visited.add((row,col))
                    banana_count += 1
                elif grid[row][col] == FRESH:
                    banana_count += 1
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        def addBanana(r,c):
            if (min(r,c) < 0 or 
                r == ROW or c == COL or
                (r,c) in visited or 
                grid[r][c] != FRESH):
                return
            q.append((r,c))
            visited.add((r,c))

        time = 0
        NEWS = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            for _ in range(len(q)):
                r , c = q.popleft()
                for direction in NEWS:
                    addBanana(r + direction[0], c + direction[1])
            time += 1

        if len(visited) < banana_count:
            return -1 
        return time -1

        