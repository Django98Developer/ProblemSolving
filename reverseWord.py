def reverseWords(str):
    revWord = ""
    list = str.split()
    list.reverse()
    for i in list:
        revWord += i+" "
        if i == list[-1]:
            revWord += i
    return f'"{revWord}"'


print(reverseWords('The lion is most danger animals'))
