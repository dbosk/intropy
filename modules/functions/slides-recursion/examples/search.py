""" Search through a list """

import input_type

def in_list(item, lst):
    """ Check if item is in lst """
    if len(lst) < 1:
        return False
    elif len(lst) == 1:
        return lst[0] == item

    middle = len(lst)//2
    if item == lst[middle]:
        return True
    elif item < lst[middle]:
        half_lst = lst[:middle] # lst[0:middle]
    else:
        half_lst = lst[middle+1:]
    return in_list(item, half_lst)


def main():
    """Test functionality"""
    l = sorted([1, 2, 4, 5, 8, 10, 18, 20, 21, 22, 30])
    x = input_type.input_type(int, "What to search for? ")
    if in_list(x, l):
        print("Yes!")
    else:
        print("No!")

if __name__ == "__main__":
    main()
