def sumStr(n1, n2):
    if n1 == "":
        n1 = "0"
    if n2 == "":
        n2 = "0"
    sum = 0
    sum += int(n1)+int(n2)
    return f'"{str(sum)}"'


print(sumStr("-5", "3"))
