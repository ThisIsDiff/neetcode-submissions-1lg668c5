class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ls = [[] for _ in range(len(nums)+1)]
        res = []

        for num in nums:
            count[num] += 1
        for num, c in count.items():
            ls[c].append(num)

        for i in range(len(ls) -1, -1, -1):
            for num in ls[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res