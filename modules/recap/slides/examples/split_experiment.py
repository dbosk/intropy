def main():
    with open("fil.txt", "r") as file:
        everything = file.read()

    lines = everything.split("\n")
    print(f"lines = {lines}")

    for line in lines:
        columns = line.split(" ")
        print(f"columns = {columns}")

if __name__ == "__main__":
    main()
