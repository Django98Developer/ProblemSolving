def oddCount(n):
    count = 0
    for i in range(0, n):
        if i % 2 != 0:
            count += 1
    return count

    # return n//2


print(oddCount(15))
