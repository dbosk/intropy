""" Experiment trying to write a file """

def main1():
    """ One way to print to a file """
    try:
        with open("test1.txt", "a") as file:
            for i in range(10):
                file.write(f"i = {i}\n")
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def main2():
    """ Another way to print to a file """
    try:
        with open("test2.txt", "w") as file:
            file.writelines(map(str, range(10)))
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

def main3():
    """ Yet another way to write to a file """
    try:
        with open("test3.txt", "w") as file:
            file.writelines([f"i = {i}\n" for i in range(10)])
    except EnvironmentError as err:
        print(f"We encountered an error: {err}")

if __name__ == "__main__":
    main1()
    main2()
    main3()
