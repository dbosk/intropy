"""Take input more easily."""

def input_type(t, prompt=""):
    """Take input, convert to type t; repeat if error."""
    while True:
        try:
            return t(input(prompt))
        except ValueError:
            if t == int:
                print(f"Sorry, can't convert to integer.")
            else:
                print(f"Sorry, can't convert to {t}.")

x = input_type(int, "x = ")
y = input_type(int, "y = ")
z = input_type(float, "z = ")
name = input_type(str, "Your name: ")

print(f"{x} + {y} = {x+y}")
print(f"z = {z}")
print(f"Your name is {name}")
