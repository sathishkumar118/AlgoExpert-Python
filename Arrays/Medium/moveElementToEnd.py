"""
Given an array and target value, the method needs to identify all instances of the target and push all of them to the end of the same array
"""
def moveElementToEnd(array, toMove):
    count = 0
    i = 0
    while i < len(array):
        if array[i] == toMove:
            array.remove(toMove)
            count += 1
        else:
            i += 1
    return array + [toMove]*count
