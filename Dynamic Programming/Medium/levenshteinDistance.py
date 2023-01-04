def levenshteinDistance(str1, str2):
    for i in range(len(str1)):
        if i >= len(str2):
            return i - len(str2) + 1
        else:
            if str1[i] != str2[i]:
                break
    if str1 != str2:
     levenshteinDistance(str[i:])
    pass
