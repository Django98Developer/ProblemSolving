def multiTable(n):
    result = ""
    for i in range(1, 11):
        if i < 10:
            result += f"{n} * {i} = {n*i}\n"
        else:
            result += f"{n} * {i} = {n*i}"

    return result


print(multiTable(10))
