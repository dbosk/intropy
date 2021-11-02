"""Hello world med tkinter"""

import tkinter as tk

def main():
    """Testprogram"""
    root = tk.Tk()
    text = tk.Label(root, text="Hello, world! Hej, världen!")
    text.pack()
    root.mainloop()
    print("Klart!")

if __name__ == "__main__":
    main()
