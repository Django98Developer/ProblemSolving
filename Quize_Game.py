
print("You are welcome in the Game .. ")

isPlay = input("Do you will play? (y/n) ")
if isPlay.lower() != "y":
    quit()

print("Let's go -->> ")
score = 0
questions = 0

questions += 1
answer = input("Q1: Is Python case sensitive when dealing with identifiers? ")
if answer.lower() == "yes":
    print("Correct ")
    score += 1
else:
    print("Oops! wronge ")

questions += 1
answer = input(
    "Q2: Python supports the creation of anonymous functions at runtime, using a construct called ______ ")
if answer.lower() == 'lambda':
    print("Correct ")
    score += 1
else:
    print("Oops! wronge ")

questions += 1
answer = input(
    "Q3: What arithmetic operators cannot be used with strings in Python? ")
if answer.lower() == '-':
    print("Correct ")
    score += 1
else:
    print("Oops! wronge ")

questions += 1
answer = input(
    "Q4: Which of these in not a core data type? (Lists - Dictionary - Tuples - Class) ")
if answer.lower() == 'class':
    print("Correct ")
    score += 1
else:
    print("Oops! wronge ")

result = (score/questions) * 100
if result >= 50:
    print(f"Congratulations *'_'* you have got score {score} with {result}% ")
else:
    print("Oops! you have failed")
