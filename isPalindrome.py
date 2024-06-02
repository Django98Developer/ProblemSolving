def isPalindrome(str):
    for i in range(len(str)):
        if str[i].lower() != str[-1-i].lower():
            return False
    return True


print(isPalindrome('AsdfdSa'))
