guess = int(input("Guess one of my favourite numbers: "))

while guess != 2 and guess != 3 and guess != 5:
    try:
        guess = int(input("Wrong, guess again: "))
    except ValueError:
        print("It's an actual number ...", end=" ")

print("Finally, that's correct!")
