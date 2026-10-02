"""A window to draw lines in with the mouse"""

import tkinter as tk


class DrawGUI(tk.Tk):
    """A window with a canvas to draw lines on with the mouse"""

    def __init__(self):
        """Create the canvas and bind the mouse to it"""
        super().__init__()

        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()

        self.x_old = None
        self.y_old = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_old_coord)

    def paint(self, event):
        """Draw a line from the previous point to this one"""
        if self.x_old is not None:
            self.draw_line(self.x_old, self.y_old, event.x, event.y)
        self.x_old = event.x
        self.y_old = event.y

    def draw_line(self, x_start, y_start, x_dest, y_dest):
        """Draw a line between two points on the canvas"""
        self.canvas.create_line(x_start, y_start, x_dest, y_dest)

    def reset_old_coord(self, _):
        """Forget the previous point, when the mouse button is released"""
        self.x_old = None
        self.y_old = None


def main():
    """Create the drawing window, then run the event loop"""
    window = DrawGUI()
    window.mainloop()


if __name__ == "__main__":
    main()
