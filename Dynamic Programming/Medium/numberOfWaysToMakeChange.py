def numberOfWaysToMakeChange(n, denoms):
    if n == 0:
        return 1
    denoms.sort()
    count = 0
    for denom in denoms:
        if n >= denom:
            count += numberOfWaysToMakeChange(n - denom, denoms)
    return count