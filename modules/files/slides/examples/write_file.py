""" Experiment trying to write a file """

def write_for():
    """ One way to print to a file """
    try:
        with open("test1.txt", "a") as file:
            for i in range(10):
                file.write(f"i = {i}\n")
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def write_print():
    """Writing to a file with print"""
    try:
        with open("test1.txt", "a") as file:
            for i in range(10):
                print(f"i = {i}", file=file)
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def write_lines():
    """ Yet another way to write to a file """
    try:
        with open("test2.txt", "w") as file:
            file.writelines([f"i = {i}\n" for i in range(10)])
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def write_text():
    """ Writing text in write mode """
    try:
        with open("test1.txt", "w") as file:
            file.write("Hej\n")
            file.write("Världen\n")
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

if __name__ == "__main__":
    write_text()
    write_for()
    write_print()
    write_lines()
