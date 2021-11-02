"""Exempelprogram för att rita"""

import tkinter as tk

class DrawGUI:
    """GUI för att rita bilder med musen"""

    def __init__(self):
        """Skapar GUI-fönstret"""
        self.window = tk.Tk()

        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack()

        self.x_old = None
        self.y_old = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords)

        self.window.mainloop()

    def paint(self, event):
        """Rita en linje mellan två punkter"""
        if self.x_old is None:
            self.x_old = event.x
            self.y_old = event.y
            return

        x_start = self.x_old
        y_start = self.y_old
        x_dest = self.x_old = event.x
        y_dest = self.y_old = event.y
        self.canvas.create_line(x_start, y_start, x_dest, y_dest)
        print(f"{x_start}, {y_start} -> {x_dest}, {y_dest}")

    def reset_coords(self, _):
        self.x_old = self.y_old = None
        print("Släppte musknappen!")

if __name__ == "__main__":
    draw = DrawGUI()
