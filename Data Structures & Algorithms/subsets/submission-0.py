class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] #list of list

        for num in nums:
            new_ls = [ls + [num] for ls in res]
            res += new_ls
        return res