class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            minimum = nums[i]
            for j in range(i, len(nums)):
                minimum = min(minimum, nums[j])
                count += minimum
        return count