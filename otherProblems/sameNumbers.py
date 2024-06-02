def sameNumbers(list):
    return True if list[0] == list[len(list)-1] else False


x = [10, 20, 59, 10, 20, 10]
print(sameNumbers(x))
