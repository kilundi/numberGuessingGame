import random

randomNumber = random.randrange(0, 11)
print(randomNumber)

guess = input("Guess a number between 0 and 10: ")

while not guess.isdigit():
    guess = input("That's not a valid number! Please enter another number: ")

guess = int(guess)

while guess != randomNumber:
    if guess > randomNumber:
        print("Too high! Guess again.")
    elif guess < randomNumber:
        print("Too low! Guess again.")

    guess = int(input("Enter a number again: "))

print(f"Congratulations! You guessed the correct number {randomNumber}.")
