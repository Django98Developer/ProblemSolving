def strCount(string, char):
    count = 0
    for i in range(0, len(string)):
        if char == string[i]:
            count += 1
    return f"This character is founded {count} times."


s = input("Enter a string : ")
c = input("Enter a character to search : ")
print(strCount(s, c))
