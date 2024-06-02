def betterThanAverage(classPoints, yourPoints):
    res = 0
    for i in range(len(classPoints)):
        res += classPoints[i]
    avg = res/len(classPoints)
    return yourPoints > avg


cp = [41, 72, 75, 56, 80, 82, 81, 33]
print(betterThanAverage(cp, 50))
