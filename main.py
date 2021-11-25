import threading
import time
import sys
from tkinter import *
from random import *
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

X, Y = 600, 600
CORNERS = [[0, 0], [X, Y//2], [0, Y]]
SPEED = 0.005
SIZE = 3
sys.setrecursionlimit(5000)

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(f"{X}x{Y}")
        self.root.title("Sierpinski Triangle")
        self.mainframe = self.createMainFrame()
        self.c = self.createCanvas()
        self.draw()
        self.x, self.y = self.createStartPoint()
        threading.Thread(target=self.do).start()

    def do(self):
        while True:
            o = self.c.create_oval(self.x - SIZE, self.y - SIZE, self.x + SIZE, self.y + SIZE, fill="white")
            time.sleep(SPEED)
            corner = choice(CORNERS)
            cx, cy = corner[0], corner[1]
            l = self.c.create_line(self.x, self.y, cx, cy, fill="white")
            self.c.delete(o)
            x, y = eval(f"{self.x}+cx")//2, eval(f"{self.y}+cy")//2
            o = self.c.create_oval(x - SIZE, y - SIZE, x + SIZE, y + SIZE, fill="white")
            time.sleep(SPEED)
            self.c.delete(l)
            self.x, self.y = x, y
            self.do()

    def createStartPoint(self):
        x, y = randint(0, X), randint(0, Y)
        point = Point(x, y)
        while not self.pol.contains(point):
            x, y = randint(0, X), randint(0, Y)
            point = Point(x, y)
        return x, y

    def draw(self):
        self.pol = Polygon([(0, 0), (X, Y//2), (0, Y)])
        self.c.create_polygon(0, 0, X, Y//2, 0, Y, outline="#ffffff", width=2)

    def createCanvas(self):
        c = Canvas(self.mainframe, width=X, height=Y, bg="#000000")
        c.pack(fill="both", expand="True")
        return c

    def createMainFrame(self):
        frame = Frame(self.root, bg="#000000")
        frame.pack(fill="both", expand="True")
        return frame

    def loop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.loop()