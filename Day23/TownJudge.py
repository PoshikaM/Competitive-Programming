def findJudge(N, trust):
    if N == 1 and not trust:
        return 1

    trusts = [0] * (N + 1)
    trusted_by = [0] * (N + 1)

    for a, b in trust:
        trusts[a] += 1
        trusted_by[b] += 1

    for i in range(1, N + 1):
        if trusts[i] == 0 and trusted_by[i] == N - 1:
            return i

    return -1