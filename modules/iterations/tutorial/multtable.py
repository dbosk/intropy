"""Print the multiplication table on screen."""

import math

# the number of spaces between columns
SPACE = 1
# the number of cells in the table
MAX_TABLE = 7 

def max_width(table_size):
    """Computes the max width based on table size, i.e. the number of digits 
    needed for the largest number.

    If table_size is 15, it requires log_10(15) digits. The table will then 
    require log_10(15*15) digits, or 2*log_10(15). We must round up."""
    return math.ceil(2*math.log(table_size, 10))

def print_header(max_table, spacing):
    """Prints the header:
    max_width characters wide,
    numbered 1, ..., max_table"""
    MAX_WIDTH = max_width(max_table)
    # top bar
    print(" "*(MAX_WIDTH-1) + "* |", end="")
    # columns
    for y in range(1, max_table+1):
        print(f"{y:{spacing+MAX_WIDTH}d}", end="")
    # break to new line
    print("")

def print_separator(max_table, spacing):
    """Prints a separating line long enough for table of size max_table with 
    spacing spacing"""
    MAX_WIDTH = max_width(max_table)
    # print a separating line
    print("-"*MAX_WIDTH + "-+" +
        "-"*((max_table+1)*(spacing+MAX_WIDTH)-MAX_WIDTH-1))

def print_row(y, x_max, spacing):
    """Prints a row in the multiplication table: y is fixed, then prints y*x 
    ... y*x_max"""
    MAX_WIDTH = max_width(x_max)

    # print the column with the vertical bar
    print(f"{y:{MAX_WIDTH}d} |", end="")

    # print the row
    for x in range(1, x_max+1):
        print(f"{x*y:{spacing+MAX_WIDTH}d}", end="")

    # break to a new line
    print("")

def print_table(max_table, spacing):
    """Prints the multiplication table sized max_table x max_table,
    columns are spaced by spacing spaces"""
    MAX_WIDTH = max_width(max_table)

    print_header(max_table, spacing)
    print_separator(max_table, spacing)

    for y in range(1, max_table+1):
        print_row(y, max_table, spacing)

print_table(MAX_TABLE, SPACE)
