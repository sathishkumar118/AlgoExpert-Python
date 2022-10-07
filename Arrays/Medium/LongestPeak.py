""" a method which takes in an array and identifies the longest peak in it.
First half of the peak will be strictly increasing whereas the second half will be strictly decreasing with the longest value - tip of the peak - remaining in the middle"""

def longestPeak(array):
    # Write your code here.
    if len(array) <3:
        return 0
    max_len = 0
    for idx in range(len(array) - 2):
        if (array[idx + 1] > array[idx] and array[idx + 1] > array[idx+2]):
            temp = idx
            count = 3
            while temp > 0:
                if array[temp] <= array[temp - 1]:
                    break
                count += 1
                temp -= 1
            temp = idx + 2
            while temp < len(array) - 1:
                if array[temp] <= array[temp + 1]:
                    break
                count += 1
                temp += 1
            if count > max_len:
                max_len = count
    return max_len
