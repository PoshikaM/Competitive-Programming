def numMovesStonesII(stones):
    stones.sort()
    n = len(stones)
    
    maxMoves = (stones[-1] - stones[0] + 1) - n
    maxMoves -= min(stones[1] - stones[0], stones[-1] - stones[-2])
    
    minMoves = float('inf')
    j = 0
    for i in range(n):
        while j < n and stones[j] - stones[i] + 1 <= n:
            j += 1
        maxInWindow = j - i
        if maxInWindow == n - 1 and stones[j-1] - stones[i] + 1 == n - 1:
            minMoves = min(minMoves, 2)
        else:
            minMoves = min(minMoves, n - maxInWindow)
    
    return [minMoves, maxMoves]

stones = [7, 4, 9]
print(numMovesStonesII(stones))