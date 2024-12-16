def maxValue(n, index, maxSum):
    def calculate_sum(x, length):
        if x >= length:
            return (x * (x + 1)) // 2 - ((x - length) * (x - length + 1)) // 2
        else:
            return (x * (x + 1)) // 2 + (length - x)
    
    def is_valid(x):
        left = calculate_sum(x - 1, index)
        right = calculate_sum(x - 1, n - index - 1)
        return left + right + x <= maxSum

    low, high = 1, maxSum
    result = 1
    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result