""" Experiment trying to open a file """

def main1():
    """ One way of reading a file """
    try:
        with open("test1.txt", "r") as file:
            print(file.read())
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def main2():
    """ Another way of reading a file """
    try:
        with open("test2.txt", "r") as file:
            for line in file.readlines():
                print(line)
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

if __name__ == "__main__":
    main1()
