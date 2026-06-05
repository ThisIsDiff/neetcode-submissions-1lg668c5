class Solution:
    def rob(self, nums: List[int]) -> int:
        # one = two = 0

        # for i in range(len(nums)):
        #     tmp =  max(nums[i] + one, two)
        #     one = two
        #     two = tmp
        if len(nums) == 1:
            return nums[0]
        return max(self.linear_rob(nums[1:]), self.linear_rob(nums[:-1]))
        
    def linear_rob(self, nums):
        one = two = 0
        for i in range(len(nums)):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp

        return two