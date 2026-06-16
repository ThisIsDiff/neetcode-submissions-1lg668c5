class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        p_stack = []
        atlantic = set()
        a_stack = []
        result = []

        ROW, COL = len(heights), len(heights[0])

        for row in range(ROW):
            for col in range(COL):
                if row == 0 or col == 0:
                    pacific.add((row,col))
                    p_stack.append((row,col))
                if row == ROW -1 or col == COL -1:
                    atlantic.add((row,col))
                    a_stack.append((row,col))

        
        def addHeight(r, c, h, visited, stack):
            if (min(r,c) < 0 or 
                r >= ROW or c >= COL or 
                (r,c) in visited or 
                heights[r][c] < h):
                return
            visited.add((r,c))
            stack.append((r,c))

        def traverse(visited, stack):
            NEWS = [(1,0), (0,1), (-1,0), (0,-1)]

            while stack:
                row, col = stack.pop()
                for dr, dc in NEWS:
                    addHeight(row + dr, col + dc, heights[row][col], visited, stack)


        traverse(pacific, p_stack)
        traverse(atlantic, a_stack)


        for loc in pacific:
            if loc in atlantic:
                result.append(loc)

        return result