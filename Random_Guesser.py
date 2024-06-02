
import random

print("Welcome ^_^ ")


def isDigit(number):
    if number.isdigit():
        number = int(number)
        if number <= 0:
            print("Please enter number greater than 0 next time.")
            # isDigit(number)
            quit()
    else:
        # isDigit(number)
        print("Please enter correct number and greater than 0 next time.")
        quit()
    return number


n = input("Plaese enter a number : ")
num = isDigit(n)

random_number = random.randint(0, num)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    user_guess = int(user_guess)
    if user_guess == random_number:
        print("Oh! you have got it")
        break
    elif user_guess > random_number:
        print("This number above correct guess")
        continue
    else:
        print("This number below correct guess")

print(f"Tries : {guesses}")
