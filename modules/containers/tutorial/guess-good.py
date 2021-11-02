"""
This is a simple guessing game.
"""

import random

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

def input_until_in_interval(prompt, interval):
    """Ask the user for input until the input is correct"""
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError as err:
            print(f"Can't convert that to an integer: {err}")
            print("Try again!")
            continue

        if in_interval(user_input, interval):
            break

    return user_input

def ask_question(question, answer, interval, max_attempts=3):
    """Asks question, returns the number of attempts to arrive at answer"""
    for attempt in range(1, max_attempts+1):
        guess = input_until_in_interval(
            f"{question} [attempt: {attempt}] ",
            interval)
        if int(guess) == answer:
            return attempt

    return max_attempts + 1


def main():
    """The main program"""
    NUM_OF_ROUNDS = 2
    NUM_OF_ATTEMPTS = 5
    INTERVAL = [0, 10]

    results = []

    for round_number in range(1, NUM_OF_ROUNDS+1):
        print(f"Round {round_number}!")

        number = random.randint(INTERVAL[0], INTERVAL[1])
        attempts = ask_question(
                "What number am I thinking of?",
                number, INTERVAL,
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
