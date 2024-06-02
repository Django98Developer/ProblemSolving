def stringToList(str):
    list = []
    res = ""
    for i in range(len(str)):
        if str[i] != " ":
            res += str[i]
        else:
            list.append(res)
            res = ""
    list.append(res)
    return list


print(stringToList("ayman gamal gamal"))
