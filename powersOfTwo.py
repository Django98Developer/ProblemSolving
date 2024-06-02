def powersOfTwo(n):
    list = []
    for i in range(0, n+1):
        list.append(2**i)
    return list


print(powersOfTwo(4))
