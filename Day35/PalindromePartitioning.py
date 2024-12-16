class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(string):
            return string == string[::-1]

        result = []
        def find_partition(index, arr):
            if index == len(s):
                result.append(list(arr))
                return

            for i in range(index, len(s)):
                string = s[index:i+1]

                if is_palindrome(string):
                    arr.append(string)
                    find_partition(i+1, arr)
                    arr.pop()

        find_partition(0, [])
        return result