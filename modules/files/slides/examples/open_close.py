""" Opening and closing files """

def read_without_with(filename):
    """ Read a file without the with statement """
    try:
        file = open(filename, "r")
        number = int(file.read())
        print(f"The number is {number}")
    except EnvironmentError as err:
        print(f"Error related to file: {err}")
    except ValueError as err:
        print(f"Error related to type conversion: {err}")
    finally:
        if file:
            file.close()

def read_with_with(filename):
    """ Read a file with the with statement """
    try:
        with open(filename, "r") as file:
            number = int(file.read())
        print(f"The number is {number}")
    except EnvironmentError as err:
        print(f"Error related to file: {err}")
    except ValueError as err:
        print(f"Error related to type conversion: {err}")

def main():
    """The main program"""
    filename = input("Please enter file name: ")

    print("without:")
    without_with(filename)

    print("with:")
    with_with(filename)

if __name__ == "__main__":
    main()

