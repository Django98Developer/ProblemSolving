def repeat(n, s):
    for i in range(1, n):
        print(s, end="")
    return s


no = 3
st = "hello"
print(repeat(no, st))
