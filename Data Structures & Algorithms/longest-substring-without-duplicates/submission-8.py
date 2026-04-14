class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        visited = {}
        length= 0  
        start = 0 
        for i, c in enumerate(s):
            if c not in visited.keys():
                length +=1
            else:
                start = max(start,visited.get(c))
                length = i - start
            visited[c] = i
            res = max(res, length)
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
