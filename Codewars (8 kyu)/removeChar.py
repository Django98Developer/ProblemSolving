def removeChar(str):
    result = ""
    for i in range(1, len(str)-1):
        result += str[i]
    return result


s = "Hello World"
print(removeChar(s))
