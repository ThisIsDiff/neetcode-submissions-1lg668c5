class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(cur_ls, i, tar):
            if tar == 0:
                res.append(cur_ls.copy())
                return
            if tar < 0 or i >= len(candidates):
                return

            num = candidates[i]
            new_ls = cur_ls + [num]
            dfs(new_ls, i + 1, tar - num)
            index = i
            while (index < len(candidates) and num == candidates[index]):
                index += 1
            dfs(cur_ls, index, tar)
            
        dfs([], 0, target)
        return res