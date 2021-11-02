"""Exmepel på inmatning med tkinter"""

import tkinter as tk

class InputGUI:
    """Klass som implementerar ett fönster för input"""

    def __init__(self):
        print("skapar fönster")
        self.window = tk.Tk()

        self.counter = 0

        print("skapar namn_label")
        self.name_label = tk.Label(self.window, text="Namn:")
        self.name_label.grid(row=0, column=0)

        print("skapar namnruta")
        self.name = tk.Entry(self.window)
        self.name.grid(row=0, column=1)

        self.output = tk.StringVar()

        print("skapar utmatningsruta")
        self.output_label = tk.Label(self.window, textvariable=self.output)
        self.output_label.grid(row=1, column=0)

        print("skapar ok-knapp")
        self.ok_button = tk.Button(self.window, text="OK",
                command=self.update_output)
        self.ok_button.grid(row=0, column=2)

        print("startar mainloop")
        self.window.mainloop()
        print("returnerat från mainloop")

    def update_output(self):
        """Uppdaterar utmatningslabelns text"""
        print("tyckte på OK!")
        self.output.set(f"Hej, {self.name.get()}! {self.counter}:a gången")
        self.counter += 1

if __name__ == "__main__":
    input_window = InputGUI()
