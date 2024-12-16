class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []
        value = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                fraction.append([arr[i], arr[j]])
                value.append(float(arr[i]) / float(arr[j]))
        dicti = dict(zip(value, fraction))
        value.sort()
        ans = dicti[value[k-1]]
        return ans