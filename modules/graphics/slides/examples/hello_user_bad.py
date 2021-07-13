"""Super ugly program"""

import tkinter as tk

def main():
    """Test program"""
    window = tk.Tk()

    # Name:
    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=0, column=0)

    # Input field
    name = tk.Entry(window)
    name.grid(row=0, column=1)

    # Output below
    output = tk.Label(window)
    output.grid(row=1, column=0)

    # Don't do this!
    def update_output():
        output["text"] = f"Hello, {name.get()}!"

    # OK button next to input field
    ok_button = tk.Button(window, text="OK",
                          command=update_output)
    ok_button.grid(row=0, column=2)

    # Run the window --- loop forever
    window.mainloop()

if __name__ == "__main__":
    main()
