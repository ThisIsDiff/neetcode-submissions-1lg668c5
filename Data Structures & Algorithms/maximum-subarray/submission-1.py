class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        sumsub = 0
        l = 0 
        for r in range(len(nums)):
            if sumsub < 0:
                l = r
                sumsub = 0
            sumsub += nums[r]
            result = max(sumsub, result)
        return result


                
            