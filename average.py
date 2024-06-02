count = int(input("Enter Count of numbers : "))
sum = 0
for i in range(count):
    x = int(input("Enter an integer : "))
    sum += x
    # avg = sum/count
print(f"The average of numbers is {sum/count}")
