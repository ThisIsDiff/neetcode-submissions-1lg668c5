class Solution:
    def trap(self, height: List[int]) -> int:
        waterArea = 0
        l = 0
        maxL = height[l]
        r = len(height) -1 
        maxR = height[r]
        while (l < r):
            if maxL < maxR :
                l += 1
                maxL = max(maxL, height[l])
                waterArea += (maxL - height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                waterArea += (maxR - height[r])
        return waterArea

            


"""
Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

highest = 3
max = 3+1+3+0+2+3+2+0+1+2 = 17
sub = 3,1,1,0,0,0,0,0,1,2

left = 0
right = len(height) - 1

height=[0,1,0,2,1,0,1,3,2,1,2,1]
max =   3+2+3+1+2+3+2+0+1+2+1+2 = 22 # this is unnesscarry just add the diffl and diffr, no need for subtraction
diffL = 3,2,2,1,1,1,1,0,0,0,0,0 = 11
diffR = 0,0,0,0,0,0,0,0,1,1,1,2 = 5
to-do
- increment l and decrement r until their height reaches the max hight
- using the maximum height as we increment/decrement to subtract from the highest peak value
"""