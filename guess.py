import random
def guessing_game():
    number = random.randint(1, 100)
    while True:
        user_guess = int(input("Guess a number between 1 to 100: "))
        if user_guess < 1 or user_guess >100:
            print("Invalid input. Please enter a number between 1 to 100")
            continue
        if user_guess < number:
            print("Too low! Try again.")
        elif user_guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break
guessing_game()

 