number = int(input("Enter an integer : "))
j = 0
if number > 1:
    for i in range(2, number-1):
        if (number % i == 0):
            j += 1
            break
    if j == 0:
        print(f"This number {number} is prime")
    else:
        print(f"This number {number} is not prime")
else:
    print(f"This number {number} is not prime")
