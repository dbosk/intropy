def main():
    with open("fil.txt", "r") as file:
        everything = file.read()

    lines = everything.split("\n")
    print(f"lines = {lines}")

    for line in lines:
        if line == "":
           continue
        columns = line.split(" ")
        num1 = int(columns[0])
        num2 = int(columns[1])
        print(f"columns = {columns}")

if __name__ == "__main__":
    main()
