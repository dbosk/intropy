""" Experiment file format """

def main_write():
    """ Writes x, f(x) pairs to a file """
    x_list = range(100)
    y_list = map(lambda x: 2*x+3, x_list)
    xy_pairs = zip(x_list, y_list)
    with open("xy.txt", "w") as file:
        for x_val, y_val in xy_pairs:
            file.write(f"{x_val} -> {y_val}\n")

def check_values(x_val, y_val):
    """ Checks if y = f(x) """
    if 2*x_val+3 != y_val:
        return False
    return True

def main_read():
    """ Reads a file of x, f(x) pairs """
    with open("xy.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        x_val, y_val = line.split(" -> ")
        if not check_values(int(x_val), int(y_val)):
            raise ValueError(f"{x_val} -/> {y_val}")
    
    print("All values looked good!")

if __name__ == "__main__":
    try:
        main_write()
        main_read()
    except Exception as err:
        print(f"An error occured: {err}")
