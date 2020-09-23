"""
This program reads names from the user and then prints them nicely aligned.
"""
# pylint: disable-msg=C0103

names = []

while True:
    name = input("Please enter a name (empty to terminate): ")
    if name == "":
        break
    names.append(name)

MAX_ROW_WIDTH = 30
MAX_NAME_WIDTH = len(max(names, key=len)) + 2
WORDS_PER_ROW = MAX_ROW_WIDTH // MAX_NAME_WIDTH

# print the words nicely aligned
for i, name in enumerate(names):
    if i % WORDS_PER_ROW == 0:
        print("")
    print(f"{name:{MAX_NAME_WIDTH}s}", end="")
print("")

