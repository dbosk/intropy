"""
This program reads names from the user and then prints them nicely aligned.
"""

def read_list(prompt, item_type=str):
    """Prints prompt, lets user input items until blank line,
    returns a list containing the items"""
    items = []
    item = input(prompt)
    while item != "":
        try:
            items.append(item_type(item))
        except TypeError as err:
            print(err)

        item = input(prompt)

    return items

def print_list(items, max_row_width=30):
    """Prints items in list items to screen, maximum max_row_width characters 
    wide"""
    # calculate the widest word to print
    # add +2 since we need spaces on each side
    MAX_ITEM_WIDTH = len(max(filter(str, names), key=len))+2
    ITEMS_PER_ROW = max_row_width // (MAX_ITEM_WIDTH)
    # print the words nicely aligned
    for count, item in enumerate(items):
        if count % ITEMS_PER_ROW == 0:
            print("")
        print(f"{item:{MAX_ITEM_WIDTH}s}", end="")
    print("")


names = read_list("Please enter a name (blank to exit): ")
print_list(names)

