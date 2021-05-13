"""A clock in the terminal"""

import sys
import time

def main():
    """The terminal clock main program"""
    while True:
        # Print the time HH:MM:SS
        # Bring the cursor back to the start of the line (8 steps)
        print(time.strftime("%H:%M:%S") + "\b"*8, end="")
        # Python only updates the terminal if enough has been printed
        # or we break the line, we won't fulfil either criteria;
        # force python to print to terminal
        sys.stdout.flush()
        # No need to update more than once per second
        time.sleep(1)

if __name__ == "__main__":
    main()
