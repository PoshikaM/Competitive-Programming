class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, arr):
            result.append(list(arr))

            for i in range(index, len(nums)):
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
        backtrack(0, [])
        return result