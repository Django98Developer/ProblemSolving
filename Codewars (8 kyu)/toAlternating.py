def toAlternatingCase(string):
    alternative = ""
    for i in range(0, len(string)):
        if string[i].isupper():
            alternative += string[i].lower()
        elif string[i].islower():
            alternative += string[i].upper()
        else:
            string[i]
    return alternative


s = "AlTeRnAtIvE"
print(toAlternatingCase(s))
