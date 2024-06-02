def decimalToBinary(num):
    if num >= 1:
        decimalToBinary(num // 2)
    print(num % 2, end=' ')


decimalToBinary(17)

# number = int(input("Enter decimal number to convert binary : "))
# print(f"The decimal number is : {number}")
# print("After converting, the binary number is : ")
# while number >= 1:
#     binary = number % 2
#     print(binary, end=' ')
#     number = number//2
