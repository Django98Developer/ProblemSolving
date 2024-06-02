def remove_spaces(string):
    remchar = ""
    for i in range(0, len(string)):
        if string[i] != " ":
            remchar += string[i]
    return remchar


chars = "ldkk hf 47 7 8jlhjl 9 llfl flh   ff"
print(remove_spaces(chars))
