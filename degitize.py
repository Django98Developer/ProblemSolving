import random


def degitize(number):
    list = []
    number = str(number)
    for n in number:
        list.append(int(n))
    list.reverse()
    return list


x = random.randrange(1000000)
print(x)
print(degitize(x))
