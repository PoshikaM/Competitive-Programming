def TargetIndices(n, arr, target):
    currentSum = 0
    sumMap = {}

    for i in range(n):
        currentSum += arr[i]

        if currentSum == target:
            return 0, i
        
        if currentSum - target in sumMap:
            startIndex = sumMap[currentSum - target] + 1
            return startIndex, i
        
        sumMap[currentSum] = i

    return None

n = int(input())
arr = list(map(int, input().split()))
target = int(input())
answer = TargetIndices(n, arr, target)
print(*answer)