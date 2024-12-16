class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            maximum = minimum = nums[i]
            for j in range(i, len(nums)):
                maximum = max(maximum, nums[j])
                minimum = min(minimum, nums[j])
                count += maximum - minimum
        return count