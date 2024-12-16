class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            maximum = nums[i]
            for j in range(1, k):
                maximum = max(maximum, nums[i+j])
            result.append(maximum)
        return result