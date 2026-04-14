class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # zero = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero.append(i)
        #         continue
        #     prod *= nums[i]
        # res = []
        # for _ in range(len(nums)):
        #     res.append(0)
        # if len(zero) == 1:
        #     nonzero = zero[0]
        #     res[nonzero] = prod
        # elif len(zero) < 1:
        #     for i in range(len(nums)):
        #         num = nums[i]
        #         res[i] = int(prod/num)
        # return res

        res = ['0'] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


        """
        - multiply as we go through the list for O(n)
        - no division
        """