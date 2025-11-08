import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 0 and 1000.")

x = random.randint(0, 1000)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < x:
            print("Higher!")
        elif guess > x:
            print("Lower!")
        else:
            print(f"Correct! 🎉 You guessed it in {attempts} tries.")
            break
    except ValueError:
        print("Please enter a valid number.")
