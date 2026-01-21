phone = {"adam": "0701234567", "bertil": "0721234567"}

name = input("Who's phone number?")

if name in phone:
    print(f"{name} has phone number {phone[name]}.")
else:
    print(f"Sorry, {name} is not in the phonebook.")
