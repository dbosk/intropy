"""
This is a simple guessing game.
"""

import random

INTERVAL = [0, 10]

def input_until(prompt, predicate=lambda _: True):
    """Ask the user for input until predicate(input) is true"""
    user_input = input(prompt)
    while not predicate(user_input):
        user_input = input(prompt)

    return user_input

def in_interval(user_input, interval):
    """Checks that user_input is a number in the correct range"""
    try:
        num = int(user_input)
    except ValueError as err:
        print(f"Sorry, couldn't convert to integer: {err}")
        return False

    if interval[0] <= num and num <= interval[1]:
        return True

    print(f"Sorry, must be in interval {interval}.")
    return False

def ask_question(question, answer, max_attempts=3):
    """Asks question, returns the number of attempts to arrive at answer"""
    for attempt in range(1, max_attempts+1):
        guess = input_until(
                f"{question} [attempt: {attempt}] ",
                lambda x: in_interval(x, [INTERVAL[0], INTERVAL[1]]))
        if int(guess) == answer:
            return attempt

    return max_attempts + 1


def main():
    """The main program"""
    NUM_OF_ROUNDS = 2
    NUM_OF_ATTEMPTS = 5

    results = []

    for round_number in range(1, NUM_OF_ROUNDS+1):
        print(f"Round {round_number}!")

        number = random.randint(INTERVAL[0], INTERVAL[1])
        attempts = ask_question(
                "What number am I thinking of?",
                number,
                NUM_OF_ATTEMPTS)

        results.append(attempts)

        if attempts > NUM_OF_ATTEMPTS:
            print("Too bad, you didn't make it.")
        else:
            print("Excellent guess!")

    average_attempts = sum(results)/NUM_OF_ROUNDS
    print(f"On average, you needed {average_attempts:.2f} tries.")

# start the main program
main()
