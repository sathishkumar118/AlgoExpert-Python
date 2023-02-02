def hasSingleCycle(array):
    length = len(array)
    visited = [False] * length
    curr = 0
    while True:
        if visited[curr] and sum(visited) == length and curr == 0:
            return True
        elif visited[curr]:
            return False
        visited[curr]  = True
        curr = (curr + array[curr]) % length
