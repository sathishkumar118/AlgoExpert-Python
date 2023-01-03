def minNumberOfCoinsForChange(n, denoms):
    arr = [0] + [float('inf')]*n
    for i in range(1, n+1):
        for d in denoms:
            if d <= i and arr[i - d] != -1:
                arr[i] = min(arr[i],arr[i - d] + 1)
    return arr[-1] if arr[-1] != float('inf') else -1