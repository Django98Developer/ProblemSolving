
def listPluslist(list1, list2):
    list1.extend(list2)
    sum = 0
    for i in range(len(list1)):
        sum += list1[i]
    return sum


L1 = [1, 2, 3]
L2 = [4, 5, 6, 3]
print(listPluslist(L1, L2))
