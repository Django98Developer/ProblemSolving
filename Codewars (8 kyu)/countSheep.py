def countSheep(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i]:
            count += 1
    return count


list = [True, False, False, True, False, True, True, True, True, False, True]
print(countSheep(list))
