"""Print the multiplication table on screen."""

import math

# the number of spaces between columns
SPACE = 1
MAX_TABLE = 8
MAX_WIDTH = math.ceil(2*math.log(MAX_TABLE, 10))

# print the top bar
print(" "*(MAX_WIDTH-1) + "* |", end="")
for y in range(1, MAX_TABLE):
  print(f"{y:{SPACE+MAX_WIDTH}d}", end="")
# break to new line
print("")

# print a separating line
print("-"*MAX_WIDTH + "-+" +
      "-"*(MAX_TABLE*(SPACE+MAX_WIDTH)-MAX_WIDTH-1))

# everything below the line
for x in range(1, MAX_TABLE):
  # print the x column with the vertical bar
  print(f"{x:{MAX_WIDTH}d} |", end="")
  
  # print the multiplications with proper spacing
  for y in range(1, MAX_TABLE):
    print(f"{x*y:{SPACE+MAX_WIDTH}d}", end="")

  # break to a new line
  print("")

