class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, 10**9
        while left <= right:
            k = (left + right) // 2
            totaltime = sum((pile + k - 1) // k for pile in piles)
            if totaltime > h: left = k + 1
            else: right = k - 1
        return left