class Solution:
    def rob(self, nums: List[int]) -> int:
        # one = two = 0

        # for i in range(len(nums)):
        #     tmp =  max(nums[i] + one, two)
        #     one = two
        #     two = tmp
        return max( nums[0],self.linear_rob(nums[1:]), self.linear_rob(nums[:-1]))
        
    def linear_rob(self, nums):
        one = two = 0
        for i in range(len(nums)):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp

        return two