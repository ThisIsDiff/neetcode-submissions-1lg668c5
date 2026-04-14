class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collection = {}

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in collection:
                return [collection[diff], n]
            collection[nums[n]] = n
        return []