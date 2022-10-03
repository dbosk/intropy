"""
This is a simple guessing game.
"""

import random

NUM_OF_ROUNDS = 2
NUM_OF_ATTEMPTS = 5

def input_guess(attempt):
    """Låter användaren mata in en gissning,
    returnerar gissningen när användaren lyckats mata in korrekt."""
    while True:
        try:
            guess = int(input(
                f"Guess the number between 0--10 (attempt {attempt}): "))
        except ValueError:
            print("Sorry, that didn't work.")
            continue

        if not(0 <= guess and guess <= 10):
            print("You should guess between 0 and 10.")
            continue

        return attempt

def guess_game(num_rounds=NUM_OF_ROUNDS, num_attempts=NUM_OF_ATTEMPTS):
    """Kör ett gissningsspel, låter användaren få num_rounds frågor."""
    results = []

    for q in range(num_rounds):
        number = random.randint(0, 10)
        for attempt in range(num_attempts):
            guess = input_guess(attempt+1)

            if guess == number:
                break

        if guess == number:
            print("Congrats, next round!")
            results.append(NUM_OF_ATTEMPTS-attempt)
        else:
            print(f"You didn't make it, the correct number was {number}.")
            results.append(0)

    return results

def main():
    """Huvudprogrammet"""
    score = sum(guess_game(NUM_OF_ROUNDS, NUM_OF_ATTEMPTS))/NUM_OF_ROUNDS
    print(f"Your average was {score:.2f}.")

if __name__ == "__main__":
    main()
