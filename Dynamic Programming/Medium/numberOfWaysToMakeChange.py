def numberOfWaysToMakeChange(n, denoms):
    arr = [1] + [0]*(n)
    for denom in denoms:
        for i in range(denom, n+1):
                arr[i] += arr[i - denom]
    return arr[-1]