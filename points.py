def points(l):
    result = 0
    for i in l:
        if i[0] > i[2]:
            result += 3
        elif i[0] < i[2]:
            result += 0
        else:
            result += 1
    return result


list = ["1:3", "4:3", "1:1"]
print(points(list))
