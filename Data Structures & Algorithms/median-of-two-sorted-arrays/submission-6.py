class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(nums2) < len(nums1):
            A = nums2
            B = nums1

        totalsize = len(nums1) + len(nums2)
        half = totalsize//2

        leftA = 0
        rightA = len(A) - 1

        while True:
            x = leftA + (rightA - leftA)//2
            y = half - x - 2

            Aleft = A[x] if x>=0 else float("-inf")
            Aright = A[x+1] if (x+1) < len(A) else float("inf")
            Bleft = B[y] if y>-1 else float("-inf")
            Bright = B[y+1] if (y+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if totalsize%2:
                    return min(Aright,Bright) #we're using right instead of left is b/c we're using the floor of right+left//2 meaning that when we separate the list the left portion is always less than right portion in a odd number of element in a list
                return (max(Aleft, Bleft) + min(Aright, Bright))/2.0
            elif (Aleft > Bright):
                rightA = x - 1 
            else:
                leftA = x + 1



"""
l
[1,2]
[3]
r
"""