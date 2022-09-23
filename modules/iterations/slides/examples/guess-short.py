guess = int(input("Guess one of my favourite numbers:"))

while guess != 2 and guess != 3 and guess != 5:
    guess = int(input("Wrong, guess again:"))

print("Finally, that's correct!")
