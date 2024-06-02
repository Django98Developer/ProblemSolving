for number in range(100, 200):
    x = number
    sum = 0
    while number != 0:
        digit = number % 10
        sum = sum+digit
        number = number//10
    if sum % 2 == 0:
        print(x)
