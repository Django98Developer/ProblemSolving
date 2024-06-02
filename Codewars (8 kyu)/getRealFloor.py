def getRealFloor(f):
    if f <= 0:
        return f
    elif f < 13:
        return f-1
    else:
        return f-2


print(getRealFloor(15))
