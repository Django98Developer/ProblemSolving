def removeExclamationMark(words):
    string = ""
    for i in words:
        if i == "!":
            continue
        else:
            string += i
    return string


words = input("Enter a string :")
print(removeExclamationMark(words))
