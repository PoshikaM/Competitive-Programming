n = int(input())
arr = list(map(int, input().split()))
target = int(input())
found = False

if n == 0:
    print(-1)
else:
    left = 0
    right = len(arr)-1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            print(left, right)
            found = True
            break
        elif(current < target):
            left += 1
        else:
            right -= 1
    if not found:
        print(-1)