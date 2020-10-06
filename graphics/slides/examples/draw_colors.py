"""Super ugly program"""

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
        
        # We want to start with black color
        self.color = "black"

        # We need to check when
        # ... mouse moves with button pressed
        # ... when button released
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_old_coord)

        # We want to group the color buttons in a frame
        self.color_frame = tk.Frame()
        # We want the frame at the bottom, so we can pack it
        self.color_frame.pack()

        self.black_button = tk.Button(self.color_frame, text="black",
                                      command=self.set_black)
        self.black_button.grid(row=0, column=0)

        self.red_button = tk.Button(self.color_frame, text="Red",
                                    command=self.set_red)
        self.red_button.grid(row=0, column=1)

    def paint(self, event):
        """ Draw a line between two points """
        # If we don't have old coordinates, we must wait for new
        if self.x_old is None:
            self.x_old = event.x
            self.y_old = event.y
            return

        # If we have old coordinates, we can draw a line
        x_start, y_start = self.x_old, self.y_old
        x_dest, y_dest = self.x_old, self.y_old = event.x, event.y
        self.canvas.create_line(x_start, y_start,
                                x_dest, y_dest, fill=self.color)

    def reset_old_coord(self, _):
        """Reset x_old and y_old to None"""
        self.x_old = self.y_old = None

    def set_black(self):
        """Change line color to black"""
        self.color = "black"

    def set_red(self):
        """Change line color to red"""
        self.color = "red"



def main():
    """Test program"""
    window = DrawGUI()

    # Run the window --- loop forever
    window.mainloop()

if __name__ == "__main__":
    main()
