def hasSingleCycle(array):
    length = len(array)
    count = 0
    curr = 0
    while True:
        if count == length and curr == 0:
            return True
        elif count == length or (curr == 0 and count > 0):
            return False
        count += 1
        curr = (curr + array[curr]) % length
