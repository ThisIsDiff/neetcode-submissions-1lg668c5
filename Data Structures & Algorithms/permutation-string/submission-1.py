class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2): return False
        # s1sorted = sorted(s1)
        # l = 0
        # r = len(s1) 
        # while (r < len(s2)+1):
        #     s2sorted = sorted(s2[l:r])
        #     if s1sorted == s2sorted:
        #         return True
        #     l +=1
        #     r += 1
        # return False
        s1collection = [0] * 26
        for char in (s1):
            s1collection[ord(char) - ord('a')] +=1

        l = 0 
        s2collection = [0] * 26

        for r in range(len(s2)):
            s2collection[ord(s2[r]) - ord('a')] += 1
            if r-l+1 > len(s1):
                s2collection[ord(s2[l]) - ord('a')] -= 1
                l += 1 

            if s2collection == s1collection:
                return True
        return False

            