"""
A Method which takes in 2D-array and returns 1D-array which has all the elements in the spiral order of the given array
"""

def spiralTraverse(array):
    # Write your code here.
    r1,c1,i,j,dir = 0,0,0,0,0
    r2,c2 = len(array)-1,len(array[0])-1
    res = []
    while r1 <= r2 and c1 <= c2:
        res.append(array[i][j])
        if dir == 0:
            if j == c2:
                dir = (dir + 1)%4
                r1 += 1
                i += 1
            else:
                j += 1
        elif dir == 1:
            if i == r2:
                dir = (dir + 1)%4
                #r2 -= 1
                c2 -= 1
                j -= 1
            else:
                i += 1
        elif dir == 2:
            if j == c1:
                dir = (dir + 1)%4
                r2 -= 1
                i -= 1
            else:
                j -= 1

        elif dir == 3:
            if i == r1:
                dir = (dir + 1)%4
                c1 += 1
                j += 1
            else:
                i -= 1
    return res
    pass
