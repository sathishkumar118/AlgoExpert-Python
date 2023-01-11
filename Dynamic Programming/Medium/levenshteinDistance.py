def levenshteinDistance(str1, str2):
    l1, l2 = len(str1), len(str2)
    arr = [[i] + [0] * l1 for i in range(l1 + 1)]
    arr[0] = [i for i in range(l2 + 1)]
    print(arr)
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            arr[i][j] = min(arr[i - 1][j], arr[i - 1][j - 1], arr[i][j - 1])
            if str1[i - 1] != str2[j - 1]:
                arr[i][j] += 1
         print(arr[-1][-1])
    return arr[-1][-1]
