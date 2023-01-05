def levenshteinDistance(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 > l2:
        temp = str1[:]
        flag = True
        while temp == str2:
            if temp == '':
                return 2*l2-l1
            if flag:
                temp = temp[1:]
                flag = False
            else:
                temp = temp[:-1]
        return l1 - len(temp)
    pass
