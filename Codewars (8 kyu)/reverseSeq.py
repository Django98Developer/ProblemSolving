def reverseSeq(n):
    list = []
    for i in range(n, 0, -1):
        list.append(i)
    return list


print(reverseSeq(5))
