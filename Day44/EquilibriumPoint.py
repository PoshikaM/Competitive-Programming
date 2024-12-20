def find_equilibrium(arr):
    n = len(arr)
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i + 1
        
        left_sum += arr[i]
    
    return -1

arr = [1, 3, 5, 2, 2]
print(find_equilibrium(arr))