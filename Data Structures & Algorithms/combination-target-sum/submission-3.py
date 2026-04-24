class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        collection = []

        def helper_combinationSum(tar, ls, index):
            nonlocal collection
            if tar < 0 or index >= len(nums):
                return 
            if tar == 0:
                collection.append(ls.copy())
                return

            num = nums[index]
            new_ls = ls + [num]
            helper_combinationSum(tar - num, new_ls,index)
            helper_combinationSum(tar, ls.copy(), index + 1)
            return
            
        helper_combinationSum(target, [], 0)
        
        return collection