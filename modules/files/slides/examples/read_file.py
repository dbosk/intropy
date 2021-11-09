""" Experiment trying to open a file """

def read_for():
    """Reading in a for loop"""
    try:
        with open("test1.txt", "r") as file:
            line = file.readline()
            while line:
                print(line, end="")
                line = file.readline()
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def read_lines():
    """ Another way of reading a file """
    try:
        with open("test1.txt", "r") as file:
            for line in file:
                print(line, end="")
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def read_all():
    """ One way of reading a file """
    try:
        with open("test1.txt", "r") as file:
            print(file.read())
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

if __name__ == "__main__":
    read_all()
    read_lines()
