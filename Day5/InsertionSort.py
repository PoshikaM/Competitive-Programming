n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    curr = arr[i]
    j = i-1

    while j >= 0 and curr < arr[j]:
        arr[j+1] = arr[j]
        j -= 1 

    arr[j+1] = curr
print(*arr)