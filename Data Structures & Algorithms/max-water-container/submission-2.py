class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        maxi = min(heights[l], heights[r]) * (r-l)
        area = lambda left, right: min(heights[left], heights[right]) * (right-left)
        while (l < r):
            maxi = max(maxi, area(l,r))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxi

        
"""
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
"""