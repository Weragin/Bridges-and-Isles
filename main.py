import tkinter as tk
from random import randint, choice
import numpy as np

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

island = tk.PhotoImage("data/ostrov0.png")
bridge_horizontal = tk.PhotoImage("data/ostrov1.png")
bridge_vertical = tk.PhotoImage("data/ostrov2.png")
empty = tk.PhotoImage("data/ostrov3.png")
currency = tk.PhotoImage("data/ostrov_kruh0.png")

SIDE = empty.width()
boxes = np.array([0])

root.geometry(f"{(SIDE+4)*8}x{(SIDE+4)*9}")


def setup():
    global boxes

    m = randint(4, 6)
    n = randint(3, 9)
    boxes = np.empty([m, n])

    for i in range(m):
        for j in range(n):
            canvas.create_image(2+i*SIDE)


canvas.after(100, setup)
root.mainloop()
