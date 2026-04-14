class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        maxi = 0
        for n in nums:
            increment = 0
            if (n-1) not in set_nums:
                while (n+increment) in set_nums:
                    increment += 1
                maxi = max(maxi, increment)

        return maxi 


"""

"""
        