class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1 
        hori = -1
        while (top <= bottom):
            hori = top + (bottom - top)//2
            if matrix[hori][0] > target:
                bottom = hori -1 
            elif matrix[hori][-1] < target:
                top = hori + 1
            else:
                break
        if not (top <= bottom):
            return False
        while (left <= right):
            vert = left + (right-left)//2
            if matrix[hori][vert] < target:
                left = vert + 1
            elif matrix[hori][vert] > target:
                right = vert - 1
            else:
                return True
        return False