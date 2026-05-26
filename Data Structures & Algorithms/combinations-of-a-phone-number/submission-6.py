class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dictionary = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

        res =[]
        def dfs(i,combination):
            if i >= len(digits):
                if len(combination):
                    res.append(combination)
                return

            letters = dictionary[digits[i]]
            for letter in letters:

                new_combination = combination + letter
                dfs(i+1, new_combination)

        dfs(0,"")
        return res

