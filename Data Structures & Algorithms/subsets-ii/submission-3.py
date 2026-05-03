class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(ls, i):
            if i>=len(nums):
                res.append(ls.copy())
                return

            # if i:
            old_i = i
            while  i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(ls, i + 1)
            new_ls = ls + [nums[i]]
            dfs(new_ls, old_i + 1)
        dfs([], 0)
        return res