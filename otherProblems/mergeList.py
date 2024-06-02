def merge_List(list1, list2):
    new_List = []
    for i in list1:
        if i % 2 != 0:
            new_List.append(i)
    for j in list2:
        if j % 2 == 0:
            new_List.append(j)

    return new_List


print(merge_List([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))
