import random

secret_number = random.randint(1,10)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess > secret_number:
        print("Your guess is too high")
    elif guess < secret_number:
        print("Your guess is too low")
    else:
        print("You guessed it right")
        print("You've won!!")
        print(f"Your total attempts are {attempts} ")
        break

