"""
This is a simple guessing game.
"""

import random

NUM_OF_ROUNDS = 2
NUM_OF_ATTEMPTS = 5
results = []

for q in range(NUM_OF_ROUNDS):
  number = random.randint(0, 10)
  for i in range(NUM_OF_ATTEMPTS):
    while True:
      try:
        guess = int(input(f"Guess the number between 0--10 (attempt {i+1}): "))
      except:
        print("Sorry, that didn't work.")
        continue
      if 0 <= guess and guess <= 10:
        break
      else:
        print("You should guess between 0 and 10.")

    if guess == number:
      break

  if guess == number:
    print("Congrats, next round!")
    results.append(NUM_OF_ATTEMPTS-i)
  else:
    print(f"You didn't make it, the correct number was {number}.")
    results.append(0)

score = sum(results)/NUM_OF_ROUNDS
print(f"Your average was {score:.2f}.")

