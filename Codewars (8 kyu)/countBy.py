def countBy(x, n):
    list = []
    for i in range(1, n):
        list.append(i * x)
    return list


print(countBy(2, 10))
