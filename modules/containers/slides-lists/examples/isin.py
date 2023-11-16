names = ["Adam", "Bertil", "Caesar"]

name = input("Namn att söka efter: ")

if name in names:
    print(f"Hittade {name} bland {names}.")
else:
    print(f"Hittade INTE {name} bland {names}.")
