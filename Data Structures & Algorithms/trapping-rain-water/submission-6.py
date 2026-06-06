class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        lmax = height[l]
        rmax = height[r]
        while l<r:
            if height[r] > height[l]:
                lmax = max(lmax, height[l])
                result += lmax - height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                result += rmax - height[r]
                r-=1
        return result

"""
sssss
"""