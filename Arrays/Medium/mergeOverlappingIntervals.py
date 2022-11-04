"""Given an array of intervals. The function should identify the overlapping ones and return the array of intervals containing all the joined overlapped intervals
"""
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals,key=lambda x: x[0])
    print(intervals)
    i = 0
    while i < len(intervals)-1:
        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
            del intervals[i+1]
        else:
            i += 1
    return intervals
