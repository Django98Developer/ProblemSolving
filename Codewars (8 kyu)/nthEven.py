def nthEven(n):
    count = 0
    for i in range(1, n):
        count += 2
    return count


print(nthEven(1001))
