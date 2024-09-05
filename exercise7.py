# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    number = 69
    guess = input("Guess a number between 1 and 100: ")
    for i in range(4):
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Invalid guess. Please enter a number between 1 and 100.")
            elif guess < number:
                print("Guess is too low.")
            elif guess > number:
                print("Guess is too high.")
            else:
                print("Congratulations, you guessed correctly!")
                return
            if i == 3:
                print("Last chance!")
            guess = input("Guess again: ")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function
guess_number()

