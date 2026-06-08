class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        stack = []
        NEWS = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    stack.append((r,c))
                    area = 0
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = 0
                        area += 1
                        for dir in NEWS:
                            drow = row + dir[0]
                            dcol = col + dir[1]

                            if  (0<= drow < len(grid) and
                                0<= dcol < len(grid[0]) and
                                (drow,dcol) not in stack and
                                grid[drow][dcol] == 1):
                                stack.append((drow,dcol))
                    result = max(result, area)
        return result  