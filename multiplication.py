count = int(input("Enter the count of real numbers :"))
product = 1
for i in range(count):
    n = float(input("Enter a real number : "))
    product *= n
print(f"The product of the real numbers is {product}")
