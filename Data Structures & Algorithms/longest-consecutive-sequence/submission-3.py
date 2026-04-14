class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0;
        set_nums = set(nums)
        maxi = 1
        for n in nums:
            increment = 1
            if (n-1) not in set_nums:
                continue
            while (n+increment) in set_nums:
                increment += 1
            maxi = max(maxi, increment+1)

        return maxi 


"""
[1,2,3,4,7,8,9,10,11]
1,2 con 2 
2,3 con 3 
3,4 con 4
4,7 con 1 maxi 4
7,8 con 2 maxi 4
8,9 con 3 maxi 4
9,10 con 4 maxi 4
10, 11 con 5 maxi 5
"""
        