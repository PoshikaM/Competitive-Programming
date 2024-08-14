n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    small = i
    for j in range(i+1, n):
        if arr[small] > arr[j]:
            small = j
    arr[i], arr[small] = arr[small], arr[i]
print(*arr)