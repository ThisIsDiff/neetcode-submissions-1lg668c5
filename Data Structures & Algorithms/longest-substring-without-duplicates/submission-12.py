class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        visited = {}
        l = 0
        for r, c in enumerate(s):
            if c in visited:
                l = max(l,visited[c]+1)
            visited[c] = r
            res = max(res, r - l + 1)
        return res
            
"""
s = "bbbb"
set = b
c = b
i = 2
l = 0
lenght = 1
max = 1

to do
- no need to remove char from index if already encounter just change the left pointer
- left pointer = visited char + 1
- cur pointer - left pointer + 1 = distance
- res = max(res, distance)
"""
