import time
import tkinter


class Colors:
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'
    BLACK = 'black'
    YELLOW = 'yellow'


class PlaygroundWindow:

    def __init__(self, window_size):
        self.window_size = window_size

        self.master = tkinter.Tk()
        self.master.title('Playground')
        self.master.protocol("WM_DELETE_WINDOW", lambda: self.master.destroy())
        self.master.bind('<Escape>', lambda e: self.master.destroy())

        self.canvas = tkinter.Canvas(self.master, width=window_size[0], height=window_size[1], background=Colors.BLACK)
        self.canvas.pack()

    def put_oval_to_canvas(self, atom):
        pos_x, pos_y, rad = atom
        o = self.canvas.create_oval(pos_x - rad, pos_y - rad, pos_x + rad, pos_y + rad, fill=Colors.GREEN)

        return o

    def update(self):
        self.master.update()

    def delete_item_from_canvas(self, item):
        self.canvas.delete(item)


def run(size, world):
    playground_window = PlaygroundWindow(size)

    while True:
        coords = world.tick()

        ovals = []
        for coord in coords:
            oval = playground_window.put_oval_to_canvas(coord)
            ovals.append(oval)

        playground_window.update()

        time.sleep(0.1)

        for oval in ovals:
            playground_window.delete_item_from_canvas(oval)
