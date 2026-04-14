class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        scounter = [0] * 52
        tcounter = [0] * 52
        matched = 52
        for i in range(len(t)):
            tcounter[self.getindex(t[i])] += 1
            if tcounter[self.getindex(t[i])] - 1 == 0:
                matched -= 1
            
        res = [-1,-1]
        sizeres = float('inf')
        l=0
        for r, char in enumerate(s):
            index = self.getindex(char)
            scounter[index] +=1
            if tcounter[index] != 0 and scounter[index] == tcounter[index]: 
                matched += 1
                temp = [l,r+1]
                
            index = self.getindex(s[l])
            while scounter[index] > tcounter[index] and l<r:
                scounter[index] -= 1
                l+=1
                temp = [l,r+1]
                index = self.getindex(s[l])

            if matched == 52 and sizeres > temp[1]-temp[0]:
                res = temp
                sizeres = temp[1]-temp[0]
            
        if matched == 52:
            return s[res[0]:res[1]]
        return ""

    def getindex(self,char):
        if (ord('a')<=ord(char)<=ord('z')):
            return ord(char) - ord('a') + 26
        else:
            return ord(char) - ord('A') 