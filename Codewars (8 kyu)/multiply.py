

def multiply(l):
    m = 1
    for i in range(0, len(l)):
        m *= l[i]
    return m


list = [5, 1, 3, 4, 2, 2, 2]
print(multiply(list))
