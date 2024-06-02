number = int(input("Enter the number : "))
sum = 0
while number != 0:
    digit = number % 10
    sum = sum+digit
    number = number//10
print(f"Sum of digits is {sum}")
