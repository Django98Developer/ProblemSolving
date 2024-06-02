def squareSum(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]**2
    return sum


numbers = [1, 2, 2, 3]
print(squareSum(numbers))
