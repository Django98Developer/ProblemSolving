def digits_Reverse(number):
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end=" ")


print('"', end=" ")
digits_Reverse(7536)
print('"', end=" ")
