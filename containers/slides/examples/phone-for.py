phonebook = {"adam": "0701234567", "bertil": "0721234567"}
phonebook["cesar"] = "0731234567"
phonebook["david"] = "0741234567"
phonebook["adam"] = "0751234567"
phonebook["johan"] = "0701234567"
phonebook["ivar"] = "0701234567"
phonebook["helge"] = "076124567"

# print the phonebook nicely aligned
i = 1
for name1 in phonebook:
    print(f"{name1:10s}", end="")
    if i % 3 == 0:
        print("")
    i += 1
print("")

# ask the user for look-ups
while True:
    name2 = input("Who's phone number? ")
    if name2 == "":
        break
    print(f"{name2} has phone number {phonebook[name2.lower()]}.")

