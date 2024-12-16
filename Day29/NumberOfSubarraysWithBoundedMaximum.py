class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def subarray(limit):
            count = 0 
            current = 0

            for i in nums:
                if i <= limit:
                    current += 1
                else:
                    current = 0
                count += current
            return count

        return subarray(right) - subarray(left - 1)