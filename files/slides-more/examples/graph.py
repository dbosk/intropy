""" Draws graphs of (x, y)-pairs """

import collections
import math

def max_diff(lst):
    """ Computes maximum difference """
    return max(lst) - min(lst)

def max_width(lst):
    """ Computes max number of digits """
    return math.ceil(math.log10(max(lst)))

def draw_y_axis(y_val, width):
    """ Prints the y-axis part of ONE line """
    print(f"{y_val:{width}d}|", end="")

def draw_y_value(delta_x):
    """ Prints * after delta_x spaces """
    print(" "*delta_x + "*", end="")

def graph(xy_pairs):
    """ Prints the graph for the (x,y)-pairs to screen """
    # Makes xy_pairs a sorted list:
    # We convert it to a list in case it's a generator
    # We sort it, because we will need that later
    xy_pairs = collections.deque(sorted(xy_pairs, reversed=True))

    # Compute max number of digits
    x_vals, y_vals = zip(*xy_pairs)
    num_width_x = max_width(x_vals)
    num_width_y = max_width(y_vals)

    # Print tip of y-axis
    print(" "*num_width_y + "^")

    # Since the list of (x,y)-pairs is sorted on y-values, we can print row by 
    # row, just skipping from y-value to y-value taking the x-value into 
    # account.
    print(" "*num_width_y + "|", end="")
    x_val, y_val = xy_pairs.popleft()
    draw_y_axis(y_val, num_width_y)
    draw_y_value(x_val)
    while xy_pairs:
        prev_y_val = y_val
        x_val, y_val = xy_pairs.popleft()
        # if the y_value is the same
        if prev_y_val != y_val:
            for _ in range(prev_y_val - y_val):
                print()
            draw_y_axis(y_val, num_width_y)
