class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = float('-inf')
        stack = []
        
        for index, height in enumerate(heights):
            left = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                left = i
                res = max(res, h*(index-i))
            stack.append((left,height))

        while stack:
            i, h = stack.pop()
            res = max(res, h*(len(heights)-i))

        return res


"""
Input: heights = [7,1,7,2,2,4,11,2,2]
interation: 1
min height = 2
current area = 8
prev area = 8
res = 8

"""