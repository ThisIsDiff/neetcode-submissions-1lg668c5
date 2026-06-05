class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two =0

        for n in nums:
            rob = max(n+ one, two)
            one = two
            two = rob

        return two

