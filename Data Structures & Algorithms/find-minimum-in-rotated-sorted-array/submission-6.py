class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums) - 1
        # res =nums[0]
        # while (left < right):
        #     mid = left + (right - left)//2
        #     res = min(nums[left], nums[right], nums[mid])
        #     if (left == mid or right == mid):
        #         break
        #     if nums[left] > nums[right]:
        #         left = mid
        #     else:
        #         right = mid 

        # return res
        return min(nums)