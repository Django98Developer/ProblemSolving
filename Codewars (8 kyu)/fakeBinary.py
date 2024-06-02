def fakeBinary(str):
    if str == "":
        return "Oops! not available with an empty string"
    res = ""
    for i in range(len(str)):
        if str[i] < '5':
            res += str[i].replace(f'{str[i]}', '0')
        else:
            res += str[i].replace(f'{str[i]}', '1')
    return f'"{res}"'


print(fakeBinary("191919"))
