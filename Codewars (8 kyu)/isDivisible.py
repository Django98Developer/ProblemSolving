def isDivisible(x, y, z):
    if x % y == 0 and x % z == 0:
        print(f"Then number {x} is divisible to two numbers {y}, {z}")
    else:
        print(f"Then number {x} is not divisible to two numbers {y}, {z}")


num1 = int(input(("Please enter the number to check : ")))
num2 = int(input(("Enter the second number : ")))
num3 = int(input(("Enter the third number : ")))


if num1 > 0 and num2 > 0 and num3 > 0:
    isDivisible(num1, num2, num3)
