"""Take input more easily."""

def input_int(prompten):
    """Take input and convert to int, repeat if fail."""
    while True:
        try:
            return int(input(prompten))
        except ValueError:
            print(f"Sorry, that's not an integer")

x = input_int("x = ")
y = input_int("y = ")

print(f"{x} + {y} = {x+y}")
