"""Program which illustrates state"""

import tkinter as tk

class InputGUI:
    """GUI which takes name input and prints 'Hello, {name}!'"""
    def __init__(self):
        self.window = tk.Tk()

        self.counter = 0

        # Name:
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0)

        # Input field next to name
        self.name = tk.Entry(self.window)
        self.name.grid(row=0, column=1)

        # OK button next to input field
        self.ok_button = tk.Button(self.window, text="OK",
                                   command=self.update_output)
        self.ok_button.grid(row=0, column=2)

        # Output below
        self.output = tk.Label(self.window)
        self.output.grid(row=1, column=0)

        # Run the window --- loop forever
        self.window.mainloop()

    def update_output(self):
        """Update the output label to what's in the name entry"""
        self.output["text"] = f"Hello, {self.name.get()}" + "!"*self.counter
        self.counter += 1


def main():
    """Test program"""
    InputGUI()

if __name__ == "__main__":
    main()
