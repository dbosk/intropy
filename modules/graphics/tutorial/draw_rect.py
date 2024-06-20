"""A drawing program, with colors"""

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

        # For rectangles, we need to check for presses
        self.x_press = self.y_press = None

        self.canvas.bind("<ButtonPress-1>", self.draw_rect)

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

        self.mode = "line"

        self.line_button = tk.Button(self.color_frame, text="Line",
                command=self.set_line)
        self.line_button.grid(row=1, column=0)

        self.rect_button = tk.Button(self.color_frame, text="Rectangle",
                command=self.set_rect)
        self.rect_button.grid(row=1, column=1)

    def paint(self, event):
        """ Draw a line between two points """
        if self.mode != "line":
            return

        print(f"move x: {event.x}, y: {event.y}, color: {self.color}")

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

    def draw_rect(self, event):
        """Draw a rectangle from corner coordinates"""
        if self.mode != "rect":
            return

        print(f"click x: {event.x}, y: {event.y}, color: {self.color}")

        # on the first press we don't draw, we do that on the second press
        if self.x_press == None:
            self.x_press = event.x
            self.y_press = event.y
            return

        x_start, y_start = self.x_press, self.y_press
        x_dest, y_dest = event.x, event.y
        # We want to reset after drawing, to get two clicks
        # Try what happens without resetting to None
        self.x_press = self.y_press = None

        self.canvas.create_rectangle(x_start, y_start,
                                     x_dest, y_dest, fill=self.color)

    def reset_old_coord(self, _):
        """Reset x_old and y_old to None"""
        print("button released")
        self.x_old = self.y_old = None

    def set_black(self):
        """Change line color to black"""
        print("change to black")
        self.color = "black"

    def set_red(self):
        """Change line color to red"""
        print("change to red")
        self.color = "red"

    def set_line(self):
        """Change drawing mode to line"""
        print("change to line")
        self.mode = "line"

    def set_rect(self):
        """Change drawing mode to rectangle"""
        print("change to rect")
        self.mode = "rect"


def main():
    """Test program"""
    window = DrawGUI()

    # Run the window --- loop forever
    window.mainloop()

if __name__ == "__main__":
    main()
