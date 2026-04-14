class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        maxi = max(nums[:k])
        appearance = k

        l = 0
        for r in range(k-1,len(nums)):
            res.append(max(nums[l:r+1]))
            l+=1
        return res


"""
to do 
- if the same # appears, the appearance counter reset
- if there's a larger #, the appearance counter reset
- 2 counters for 2 numbers
"""