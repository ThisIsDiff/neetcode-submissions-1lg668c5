class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxi = float('-inf')
        window = []
        l = 0
        for r in range(k-1,len(nums)):
            sortls = sorted(nums[l:r+1])
            res.append(sortls[-1])
            l+=1


        return res