"""Hello world with tkinter"""

import tkinter as tk

def main():
    """Test program"""
    root = tk.Tk()
    text = tk.Label(root, text="Hello, world!")
    text.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
