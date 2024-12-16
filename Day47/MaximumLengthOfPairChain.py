def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])

    current_end = float('-inf')
    chain_length = 0

    for pair in pairs:
        if pair[0] > current_end:
            chain_length += 1
            current_end = pair[1]
    
    return chain_length

pairs = [[1, 2], [2, 3], [3, 4]]
print(findLongestChain(pairs))