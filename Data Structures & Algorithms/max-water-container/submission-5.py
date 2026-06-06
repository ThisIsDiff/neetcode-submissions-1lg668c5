class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) -1 

        while l<r:
            height_l = heights[l]
            height_r = heights[r]
            result = max(result, self.calArea(l,r,height_l, height_r))
            if height_l < height_r:
                l +=1
            else:
                r -=1 
        return result

    def calArea(self, left, right, lHeight, rHeight):
        return min(lHeight, rHeight) * (right-left)
