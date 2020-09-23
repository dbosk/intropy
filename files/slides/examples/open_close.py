""" Opening and closing files """

def without_with():
    """ Read a file without the with statement """
    filename = input("Please enter file name: ")
    try:
        file = open(filename, "r")
        number = int(file.read())
        print(f"The number is {number}")
    except EnvironmentError as err:
        print(f"Error related to file: {err}")
    except ValueError as err:
        print(f"Error related to type conversion: {err}")
    if file:
        file.close()

def with_with():
    """ Read a file with the with statement """
    filename = input("Please enter file name:")
    try:
        with open(filename, "r") as file:
            number = int(file.read())
        print(f"The number is {number}")
    except EnvironmentError as err:
        print(f"Error related to file: {err}")
    except ValueError as err:
        print(f"Error related to type conversion: {err}")

if __name__ == "__main__":
    print("without:")
    without_with()
    print("with:")
    with_with()
