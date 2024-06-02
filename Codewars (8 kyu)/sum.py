
def sum(list):
    if len(list) > 1:
        list.sort()
        result = 0
        for i in range(1, len(list)-1):
            result += list[i]
    else:
        return 0
    return result


arr = [6, 2, 1, 8, 10]
print(sum(arr))
