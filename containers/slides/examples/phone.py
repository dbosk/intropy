phone = {"adam": "0701234567", "bertil": "0721234567"}

while True:
  name = input("Who's phone number?").lower()
  if name == "":
    break
  try:
    print(f"{name} has phone number {phone[name]}.")
  except KeyError as err:
    print(f"Sorry, {name} is not in the phone book.")
  except Exception as err:
    print(f"Unexpected error: {err}")

