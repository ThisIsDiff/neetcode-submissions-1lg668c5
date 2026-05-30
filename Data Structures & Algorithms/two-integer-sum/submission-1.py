class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], i]
            left = target - num
            dictionary[left] = i
        return