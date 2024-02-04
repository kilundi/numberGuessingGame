import random

def get_valid_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("That's not a valid number! Please enter another number.")

randomNumber = random.randrange(0, 11)
print(randomNumber)

guesses = 0
guess = get_valid_input()

while guess != randomNumber:
    guesses += 1
    if guess > randomNumber:
        print("Too high! Guess again.")
    elif guess < randomNumber:
        print("Too low! Guess again.")

    guess = get_valid_input()

print(f"Congratulations! You guessed the correct number {randomNumber}.")
print(f"You got it in only {guesses} tries!")


# import random

# randomNumber = random.randrange(0, 11)
# print(randomNumber)

# guess = input("Guess a number between 0 and 10: ")
# guesses=0
# while not guess.isdigit():
#     guess = input("That's not a valid number! Please enter another number: ")

# guess = int(guess)

# while guess != randomNumber:
#     guesses+=1
#     if guess > randomNumber:
#         print("Too high! Guess again.")
#     elif guess < randomNumber:
#         print("Too low! Guess again.")

#     guess = int(input("Enter a number again: "))

# print(f"Congratulations! You guessed the correct number {randomNumber}.")
# print(f"You got it in only {guesses} tries!")