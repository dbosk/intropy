phone = {"adam": "0701234567", "bertil": "0721234567"}

name = input("Who's phone number?")

try:
    print(f"{name} has phone number {phone[name]}.")
except KeyError:
    print(f"Sorry, {name} is not in the phonebook.")
