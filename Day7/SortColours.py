n = int(input())
arr = list(map(int, input().split()))
left, mid, right = 0, 0, n-1

while mid <= right:
    if arr[mid] == 0:
        arr[left], arr[mid] = arr[mid], arr[left]
        left += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[right], arr[mid] = arr[mid], arr[right]
        right -= 1
print(*arr)