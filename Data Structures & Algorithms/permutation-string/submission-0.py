class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1sorted = sorted(s1)
        l = 0
        r = len(s1) 
        while (r < len(s2)+1):
            s2sorted = sorted(s2[l:r])
            if s1sorted == s2sorted:
                return True
            l +=1
            r += 1
        return False