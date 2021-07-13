"""A simple clock with tkinter"""

import tkinter as tk
import time

class Clock(tk.Tk):
    """Class for a clock application"""
    def __init__(self):
        super().__init__()

        # We'll store the time here
        self.current_time = tk.StringVar()

        # We'll use this label to print the time
        self.clockface = tk.Label(textvariable=self.current_time)
        self.clockface.pack()

        # Start the series of updating
        self.update_time()

    def update_time(self):
        """Updates the time variable, schedules new update"""
        self.current_time.set(time.strftime("%H:%M:%S"))
        # after 1000 ms (=1 s) we must update the time again
        # we get the .after method from the tk.Tk class
        self.after(1000, self.update_time)

def main():
    """Test program for our clock application"""
    clock = Clock()
    clock.mainloop()

if __name__ == "__main__":
    main()
