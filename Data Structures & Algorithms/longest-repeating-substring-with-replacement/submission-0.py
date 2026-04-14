class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        collection = {}
        l = 0
        res = 0
        for i in range(len(s)):
            collection[s[i]] = collection.get(s[i],0) + 1
            while ((i-l+1)-max(collection.values())) > k and l<=i:
                collection[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)

        return res
            