class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = nums1 + nums2
        ls.sort()

        mid = len(ls)//2
        if len(ls)%2 == 0:
            return (ls[mid] + ls[mid-1])/2
        else:
            return ls[mid]
        # left = 0
        # right = len(nums1)+len(nums2) - 1

        # while (left <= right):
        #     mid = left + (right - left)//2


"""
l
[1,2]
[3]
r
"""