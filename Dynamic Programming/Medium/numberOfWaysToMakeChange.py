def numberOfWaysToMakeChange(n, denoms, child = False):
    if n == 0:
        return 1
    count = 0
    combs = []
    for denom in denoms:
        if n == denom:
            combs.append([denom])
        elif n > denom:
            lst = numberOfWaysToMakeChange(n - denom, denoms, True)
            for elem in lst:
                elem.append(denom)
                elem.sort()
                if elem not in combs:
                    combs.append(elem)
    print(combs)
    if child:
        return combs
    else:
        return len(combs)