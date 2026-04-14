class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res =nums[0]
        while (left < right):
            mid = left + (right - left)//2
            res = min(nums[left], nums[right], nums[mid])

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return res
