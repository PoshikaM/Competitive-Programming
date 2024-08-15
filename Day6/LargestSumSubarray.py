n = int(input())
arr = list(map(int, input().split()))
current = maximum = arr[0]
if n == 0:
    print(0)
else:
    for i in arr[1:]:
        current = max(i, current+i)
        maximum = max(current, maximum)
    print(maximum)