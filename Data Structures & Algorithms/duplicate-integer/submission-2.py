class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = set(nums)

        if (len(ls) < len(nums)):
            return True

        return False