class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'(':')', '[':']', '{':'}'}
        for p in s:
            if p in dictionary.keys():
                stack.append(p)
            elif stack and dictionary[stack[-1]] == p:
                stack.pop()
            elif (stack and dictionary[stack[-1]] != p) or (not stack and p not in dictionary.keys()):
                return False
        return True if len(stack) == 0 else False