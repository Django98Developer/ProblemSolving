def row_pattern(row):
    for num in range(row):
        for i in range(num):
            print(num, end=" ")
        print("\n")


row_pattern(10)
