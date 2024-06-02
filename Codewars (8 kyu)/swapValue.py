def swapValue(values):
    swap = values[0]
    values[0] = values[1]
    values[1] = swap
    return values


list = [2, 3]
print(swapValue(list))
