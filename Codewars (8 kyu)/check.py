def check(list, val):
    for i in range(len(list)):
        if list[i] == val:
            return True
    return False


L = [1, 2, 3, 's', 'r', 'str']
print(check(L, 3))
