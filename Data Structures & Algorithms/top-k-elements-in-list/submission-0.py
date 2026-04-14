class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        collections = [[] for i in range(len(nums)+1)] #add 1 b/c what if every num in nums are the same

        for num in nums:
            counter[num] = counter.get(num,0) + 1

        for num, freq in counter.items():
            collections[freq].append(num)

        res = []

        for i in range(len(collections)-1, -1, -1):
            for j in collections[i]:
                if len(res) == k:
                    return res
                res.append(j)

        return res

        
        