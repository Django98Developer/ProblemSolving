def twiceAsOld(dad, son):
    son2x = son*2
    dadage = dad-son2x
    if dadage < 0:
        dadage *= -1
    return dadage


print(twiceAsOld(55, 30))
