while True:
  table = input("Which multiplication table? ")
  if table == "":
    break

  try:
    x = int(table)
  except ValueError as err:
    print(f"Please enter a number: {err}")
    continue

  if x > 9:
    print(f"Please enter a number less than 10")
    continue

  for y in range(1, 10):
    print(f"{x:1d}*{y:1d} = {x*y:2d}")

