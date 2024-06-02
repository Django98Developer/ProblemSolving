def zeroFuel(distanceToPump, mpg, fuelLeft):
    return fuelLeft*mpg >= distanceToPump


print(zeroFuel(50, 25, 2))
