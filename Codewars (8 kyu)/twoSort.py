def twoSort(l):
    l.sort()
    x = l[0]
    res = ""
    for i in range(len(x)):
        if i < len(x)-1:
            res += x[i] + "***"
        else:
            res += x[i]
    return res


list = ['ztr', 'uasd', 'aytr']
print(twoSort(list))
