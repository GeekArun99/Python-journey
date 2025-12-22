import random
Level = input("Enter the level you want to play (easy/hard): ").lower()

def set_attempts(level):
    if level == "easy":
        return 10
    else:
        return 5
    
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts_remaining = set_attempts(Level)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess < number_to_guess:
            print("Too low.")
            print("Guess again.")
        elif guess > number_to_guess:
            print("Too high.")
            print("Guess again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            return
        
        attempts_remaining -= 1
        
        if attempts_remaining == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}. Better luck next time!")


number_guessing_game()  
while input("Do you want to play again? Type 'yes' or 'no': ").lower() == 'yes':
    number_guessing_game()