def bonusTime(salary, bonus):
    if bonus == True:
        return f"${salary*10}"
    else:
        return f"${salary}"


print(bonusTime(10000, True))
