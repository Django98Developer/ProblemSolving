print("Enter 10 numbers")
n = 0
sum = 0
while n < 10:
    x = float(input(f"Number of {n+1}: "))
    sum += x
    n += 1
avg = sum/10
print("The average is ", avg)
