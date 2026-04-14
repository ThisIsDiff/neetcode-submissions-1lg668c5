class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        collection = {}
        l = 0
        res = 0
        maxf = 0
        for i in range(len(s)):
            collection[s[i]] = collection.get(s[i],0) + 1
            maxf = max(maxf, collection[s[i]])
            while ((i-l+1)-maxf) > k:
                collection[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)

        return res
            