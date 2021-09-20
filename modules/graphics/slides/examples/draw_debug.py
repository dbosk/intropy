"""A drawing program"""

import tkinter as tk

class DrawGUI(tk.Tk):
    """GUI which takes name input and prints 'Hello, {name}!'"""
    def __init__(self):
        # Initialize tk.Tk itself
        super().__init__()

        # Create a large canvas to draw on
        self.canvas = tk.Canvas(width=800, height=600, bg="white")
        self.canvas.pack()

        # We use lines to paint, those need two coordinates
        self.x_old = self.y_old = None

        # We need to check when
        # ... mouse moves with button pressed
        # ... when button released
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_old_coord)

    def paint(self, event):
        """ Draw a line between two points """
        # To see just how many events we get
        print(f"x: {event.x}, y: {event.y}")

        # If we don't have old coordinates, we must wait for new
        if self.x_old is None:
            self.x_old = event.x
            self.y_old = event.y
            return

        # If we have old coordinates, we can draw a line
        x_start, y_start = self.x_old, self.y_old
        x_dest, y_dest = self.x_old, self.y_old = event.x, event.y
        self.canvas.create_line(x_start, y_start,
                                x_dest, y_dest)

    def reset_old_coord(self, _):
        """Reset x_old and y_old to None"""
        print("button released")
        self.x_old = self.y_old = None



def main():
    """Test program"""
    window = DrawGUI()

    # Run the window --- loop forever
    window.mainloop()

if __name__ == "__main__":
    main()
