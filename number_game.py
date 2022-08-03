import random

print("Welcome to the Number guessing game!")
ques = input("Start new game: Type Y for yes and N for no\n")

if ques == "Y":
    guessed_number = random.randint(0,1)
    user_input = int(input("Guess a number between 0 to 1: "))
    if user_input == guessed_number:
        print("You guessed the correct number")
    else:
        print("Whooos. the number I guessed was,", guessed_number)
elif ques == "N":
    print("See you again")
else:
    print("I dont know what you want")


