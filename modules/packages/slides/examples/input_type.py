"""Take input more easily."""

def input_type(the_type, prompt=""):
    """Take input, convert to type the_type; repeat if error."""
    while True:
        try:
            return the_type(input(prompt))
        except ValueError:
            if the_type == int:
                print(f"Sorry, can't convert to integer.")
            else:
                print(f"Sorry, can't convert to {the_type}.")

def main():
    """Test functionality of this module"""
    x = input_type(int, "x = ")
    y = input_type(int, "y = ")
    z = input_type(float, "z = ")
    name = input_type(str, "Your name: ")

    print(f"{x} + {y} = {x+y}")
    print(f"z = {z}")
    print(f"Your name is {name}")

if __name__ == "__main__":
    main()
