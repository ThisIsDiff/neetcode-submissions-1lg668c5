class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two =0

        for i in range(len(nums)):
            rob = max(nums[i]+ one, two)
            one = two
            two = rob

        return two

