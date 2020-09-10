"""Print the multiplication table on screen."""

# the number of spaces between columns
SPACE = 1

# print the top bar
print("* |", end="")
for y in range(1, 10):
  print(f"{y:{SPACE+2}d}", end="")
print("")

# print a separating line
print("--+" + "-"*(10*(SPACE+2)-3))

# everything below the line
for x in range(1, 10):
  # print the x column with the vertical bar
  print(f"{x:1d} |", end="")
  
  # print the multiplications with proper spacing
  for y in range(1, 10):
    print(f"{x*y:{SPACE+2}d}", end="")

  # break to a new line
  print("")

