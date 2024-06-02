def max(list):
    maximum = list[0]
    for i in range(0, len(list)):
        if list[i] > maximum:
            maximum = list[i]
    return f"The number maximum in List is {maximum}"


def min(list):
    minimum = list[0]
    for j in range(0, len(list)):
        if list[j] < minimum:
            minimum = list[j]
    return f"The number minimum in List is {minimum}"


# s = [100, 200, 450, 650, 400, 700, 50]
s = []
L = int(input("Enter the length of List : "))
for x in range(0, L):
    s.append(int(input(f"Enter item no. {x+1}: ")))
# int(list)
print(max(s))
print(min(s))
