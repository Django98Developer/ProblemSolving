def basicOp(char, val1, val2):
    if char == '+':
        return val1+val2
    elif char == '-':
        return val1-val2
    elif char == '*':
        return val1*val2
    elif char == '/':
        return val1/val2
    else:
        print("Oops! Wronge result.")


print(basicOp("/", 3, 5))
