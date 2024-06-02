def average(l):
    sum = 0
    if len(l) >= 1:
        for i in range(len(l)):
            sum += l[i]
        return sum/len(l)
    else:
        return 0


list = [2, 2, 4, 5, 6]
print(average(list))
