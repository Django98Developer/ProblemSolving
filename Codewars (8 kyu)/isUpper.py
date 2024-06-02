
def isUpper(string):
    for i in range(0, len(string)):
        if string[i].islower():
            return False
    return True


print(isUpper("HeLLO"))  # false
print(isUpper("HELLO"))  # true
