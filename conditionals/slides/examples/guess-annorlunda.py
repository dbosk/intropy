guess = int(input("Guess one of my favourite numbers:"))

while True:
    if guess == 2 or guess == 3 or guess == 5:
        break

    guess = int(input("Wrong, guess again:"))

print("Finally, that's correct!")
