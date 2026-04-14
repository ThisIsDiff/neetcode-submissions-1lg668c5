class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = [("(",1,0)]
        while (queue):
            st, openp, closep = queue.pop(0)
            if openp < n:
                queue.append((st+"(", openp+1, closep))
                
            if closep < openp:
                queue.append((st+")",openp,closep+1))

            if closep == n:
                res.append(st)

        return res
        
"""
((()))
(()())
(()())()
()(()())
()()()
"""