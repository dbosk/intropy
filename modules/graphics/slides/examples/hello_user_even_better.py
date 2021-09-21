"""tkinter by inheritance, tkinter variables"""

import tkinter as tk

class InputGUI(tk.Tk):
    """GUI which takes name input and prints 'Hello, {name}!'"""
    def __init__(self):
        # Initialize tk.Tk itself
        super().__init__()

        # Name:
        self.name_label = tk.Label(text="Name:")
        self.name_label.grid(row=0, column=0)

        # Input field next to name
        self.name = tk.Entry()
        self.name.grid(row=0, column=1)

        # OK button next to input field
        self.ok_button = tk.Button(text="OK",
                                   command=self.update_output)
        self.ok_button.grid(row=0, column=2)

        self.output = tk.StringVar()

        # Output below
        self.output_label = tk.Label(textvariable=self.output)
        self.output_label.grid(row=1)

    def update_output(self):
        """Update the output label to what's in the name entry"""
        self.output.set(f"Hello, {self.name.get()}!")


def main():
    """Test program"""
    window = InputGUI()

    # Run the window --- loop forever
    window.mainloop()

if __name__ == "__main__":
    main()
