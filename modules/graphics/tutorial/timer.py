"""A simple timer with tkinter"""

import tkinter as tk

class Timer(tk.Tk):
    """Class for a timer application"""
    def __init__(self):
        super().__init__()

        # We'll store the time here
        self.hour = tk.IntVar()
        self.minute = tk.IntVar()
        self.second = tk.IntVar()

        # We'll use this label to print the time
        self.hour_box = tk.Entry(textvariable=self.hour)
        self.hour_box.grid(row=0, column=0)

        self.min_box = tk.Entry(textvariable=self.minute)
        self.min_box.grid(row=0, column=1)

        self.sec_box = tk.Entry(textvariable=self.second)
        self.sec_box.grid(row=0, column=2)

        # Start the series of updating
        self.update_timer()

    def update_timer(self):
        """Updates the timer"""
        # If we're not at zero, count down
        if self.hour.get() != 0 or \
           self.minute.get() != 0 or \
           self.second.get() != 0:
            self.count_down()

        # after 1000 ms (=1 s) we must update the time again
        # we get the .after method from the tk.Tk class
        self.after(1000, self.update_timer)

    def count_down(self):
        """Decrease one second, update minutes and hours when needed"""
        second = self.second.get()
        if second > 0:
            self.second.set(second-1)
            return

        minute = self.minute.get()
        if minute > 0:
            self.minute.set(minute-1)
            self.second.set(59)
            return

        hour = self.hour.get()
        if hour > 0:
            self.hour.set(hour-1)
            self.minute.set(59)
            self.second.set(59)

def main():
    """Test program for our timer application"""
    timer = Timer()
    timer.mainloop()

if __name__ == "__main__":
    main()
