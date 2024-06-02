while 1:
    reverse = 0
    number = int(input("Enter an integer : "))
    while number != 0:
        digit = number % 10
        reverse = (reverse*10)+digit
        number = number//10
    print(f"Then the number in reverse manner is {reverse}")
