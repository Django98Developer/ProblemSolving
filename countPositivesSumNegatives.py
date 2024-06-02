def countPositivesSumNegatives(list):
    count = 0
    sum = 0
    for i in list:
        if i < 0:
            sum += i
        if i > 0:
            count += 1
    return [count, sum]


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(countPositivesSumNegatives(L))
