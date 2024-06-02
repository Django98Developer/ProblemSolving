def sumOfDiffernce(list):
    list.sort(reverse=True)
    sum = 0
    if len(list) <= 1:
        return sum
    else:
        for i in range(len(list)-1):
            sum += (list[i]-list[i+1])
    return sum


L = [2, 1, 10]
print(sumOfDiffernce(L))
