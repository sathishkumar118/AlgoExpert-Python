"""Given an array of intervals. The function should identify the overlapping ones and return the array of intervals containing all the joined overlapped intervals
"""
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    i = 0
    while i < len(intervals):
        start = intervals[i][0]
        end = intervals[i][1]
        j = 0
        while j < len(intervals):
            if i != j:
                print(i,j)
                if end >=  intervals[j][0] and start <= intervals[j][0]:
                    intervals[i][1] = intervals[j][1]
                    end = intervals[i][1]
                    del intervals[j]
                    j -= 1
                    if j < i:
                        i -= 1
                elif end <= intervals[j][1] and start >= intervals[j][0]:
                    del intervals[i]
                    i -= 1
                    break
            j += 1
        i += 1
    return intervals
