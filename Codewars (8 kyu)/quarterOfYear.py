def quarterYear(month):
    if month < 4:
        return "This first quarter"
    elif month >= 4 and month < 7:
        return "This second quarter"
    elif month >= 7 and month < 10:
        return "This third quarter"
    elif month >= 9 and month < 13:
        return "This fourth quarter"
    else:
        return "Error !"


m = int(input("Enter a month : "))
print(quarterYear(m))
