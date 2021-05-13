phonebook = {"adam": "0701234567", "bertil": "0721234567"}
phonebook["cesar"] = "0731234567"
phonebook["david"] = "0741234567"

i = 1
for name in phonebook:
    print(f"{name:10s}", end="")
    if i % 5 == 0:
        print("")
print("")

while True:
    name = input("Who's phone number? ")
    if name == "":
        break
    print(f"{name} has phone number {phonebook[name]}.")

