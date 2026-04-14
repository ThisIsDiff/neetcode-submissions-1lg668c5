class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tcount, window = {}, {}
        window = {}
        for c in t:
            tcount[c] = tcount.get(c,0) + 1
        need = len(tcount)
        have , l = 0, 0
        res = [-1,-1]
        lenres = float('inf')
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in tcount and tcount[char] == window[char]:
                have += 1

            while have == need:
                if (r-l+1) < lenres:
                    res = [l,r]
                    lenres = r-l+1

                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -=1 
                l += 1
        return s[res[0]:res[1]+1] if lenres != float('inf') else ""
