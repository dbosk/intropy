"""Take input more easily."""

def input_type(t, prompt=""):
    """Take input and convert to type t, repeat if error."""
    while True:
        try:
            return t(input(prompt))
        except ValueError:
            print(f"Sorry, that can't be converted to {t}")

x = input_type(int, "x = ")
y = input_type(int, "y = ")

print(f"{x} + {y} = {x+y}")
