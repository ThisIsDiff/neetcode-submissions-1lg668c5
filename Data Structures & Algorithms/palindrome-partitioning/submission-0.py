class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return


            for j in range(i,len(s)):
                if self.isPal(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res
        
    def isPal(self,st):
        length = len(st)
        for i in range(length//2):
            if st[i] != st[length - i -1]:
                return False
        return True