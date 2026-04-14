class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1i,0l,0,1r]

        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1 
            while (l < r):
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1

        return res
        