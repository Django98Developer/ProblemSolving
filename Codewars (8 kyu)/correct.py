def correct(s):
    return s.replace("1", "I").replace("0", "O").replace("5", "S")


a = "105"
print(correct(a))