"""Take input more easily."""

def input_int(prompt="Please enter something: "):
    """Take input and convert to int, repeat if error."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"Sorry, that's not an integer")

x = input_int("x = ")
y = input_int()

print(f"{x} + {y} = {x+y}")
