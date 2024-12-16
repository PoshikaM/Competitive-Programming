class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        corres_string ={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        result = []
        def backtrack(index, string):
            if index == len(digits):
                result.append(string)
                return

            temp_string = corres_string[digits[index]]
            for i in temp_string:
                backtrack(index+1, string+i)

        backtrack(0, "")
        return result