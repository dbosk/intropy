phonebook = {"adam": "0701234567", "bertil": "0721234567"}
phonebook["cesar"] = "0731234567"
phonebook["david"] = "0741234567"

for name in phonebook:
    print(f"{name:10s}", end="")

name = input("Who's phone number? ")
while name != "":
    print(f"{name} has phone number {phonebook[name]}.")
    name = input("Who's phone number? ")

