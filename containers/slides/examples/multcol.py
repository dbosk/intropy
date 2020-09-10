"""Print the multiplication columns on screen."""

while True:
  table = input("Which multiplication table? ")
  # exit if the user just hits enter
  if table == "":
    break

  # try to convert to integer
  try:
    x = int(table)
  except ValueError as err:
    print(f"Please enter a number: {err}")

  # check that it's not a huge integer
  if x > 9:
    print(f"Please enter a number less than 10")
    continue

  # print the column of multiplications
  for y in range(1, 10):
    print(f"{x:1d}*{y:1d} = {x*y:2d}")

