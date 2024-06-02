def abbrevName(name):
    for i in range(len(name)):
        char1 = name[0].upper()
        if name[i] == " ":
            char2 = name[i+1].upper()
    return f'"{char1}.{char2}"'

# char = ""
# char += name[0].upper()
# char += "."
# char += name[name.find(" ")+1].upper()
# return f'"{char}"'


print(abbrevName("ayman gamal"))
