import random

def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 20)
    attempts = 0  # Track how many guesses the user has made

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    
    while True:
        try:
            # Step 2: Get the user's guess
            user = int(input("Enter your guess: "))
            attempts += 1

            # Step 3: Check the guess
            if user < secret_number:
                print("Too low! Try again.")
            elif user > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Run the game
number_guessing_game()
