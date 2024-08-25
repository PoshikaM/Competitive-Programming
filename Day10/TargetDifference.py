def difference(n, arr, target):
    left = 0
    right = 1

    while left<n and right<n:
        current = arr[right] - arr[left]

        if current == target:
            return 1
        elif current < target:
            right += 1
        else:
            left += 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
target = int(input())
answer = difference(n, arr, target)
print(answer)