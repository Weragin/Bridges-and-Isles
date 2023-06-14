import tkinter as tk
from random import randint

root = tk.Tk()


canvas = tk.Canvas(root, background="grey", width=416, height=468)
canvas.pack()

island = tk.PhotoImage(file="ostrov0.png")
bridge_horizontal = tk.PhotoImage(file="ostrov1.png")
bridge_vertical = tk.PhotoImage(file="ostrov2.png")
empty = tk.PhotoImage(file="ostrov3.png")
currency = tk.PhotoImage(file="ostrov_kruh0.png")
isle_currency = tk.PhotoImage(file="ostrov_kruh1.png")
sell = tk.PhotoImage(file="ostrov_kruh2.png")

SIDE = empty.width()

islands = []
bridges_h = []
bridges_v = []
empties = []
field_status = False
money = 0
coin = 0
label = 0


def click(e):
    global empties, bridges_h, bridges_v, label, field_status, money
    canvas.unbind("<1>")
    for overlap in canvas.find_overlapping(e.x, e.y, e.x, e.y):
        if field_status == 2:
            if overlap in bridges_v:
                money += 1
                canvas.itemconfig(label, text=f"{money}")
                bridges_v.remove(overlap)
                empties.append(overlap)
                canvas.itemconfig(overlap, image=empty)

            if overlap in bridges_h:
                money += 1
                canvas.itemconfig(label, text=f"{money}")
                bridges_h.remove(overlap)
                empties.append(overlap)
                canvas.itemconfig(overlap, image=empty)

        else:
            if overlap in empties and coin > 0:
                empties.remove(overlap)
                if field_status == 1:
                    money -= 2
                    canvas.itemconfig(label, text=f"{money}")
                    islands.append(overlap)
                    canvas.itemconfig(overlap, image=island)
                if field_status == 0:
                    money -= 1
                    canvas.itemconfig(label, text=f"{money}")
                    bridges_v.append(overlap)
                    canvas.itemconfig(overlap, image=bridge_vertical)

            elif overlap in bridges_v:
                bridges_v.remove(overlap)
                bridges_h.append(overlap)
                canvas.itemconfig(overlap, image=bridge_horizontal)

            elif overlap in bridges_h:
                bridges_h.remove(overlap)
                bridges_v.append(overlap)
                canvas.itemconfig(overlap, image=bridge_vertical)

        if "button" in canvas.gettags(overlap):
            field_status = (field_status + 1) % 3
            if field_status == 0:
                canvas.itemconfig(coin, image=currency)
            elif field_status == 1:
                canvas.itemconfig(coin, image=isle_currency)
            elif field_status == 2:
                canvas.itemconfig(coin, image=sell)
    canvas.bind("<1>", click)


def setup():
    global islands, empties, coin, label, money

    m = randint(4, 6)
    n = randint(3, 9)
    canvas.config(width=m*SIDE + m + 70, height=n*SIDE + n)

    for i in range(m):
        for j in range(n):
            rng = randint(0, 4)
            if rng == 0:
                islands.append(canvas.create_image(3 + i*(SIDE+1), 3+j*(SIDE+1), anchor="nw", image=island))
            else:
                empties.append(canvas.create_image(3 + i*(SIDE+1), 3+j*(SIDE+1), anchor="nw", image=empty))
    money = int(m*n//2.5)
    coin = canvas.create_image((m + 1)*SIDE - 6, 4 + SIDE//2, image=currency, tags="button")
    label = canvas.create_text((m + 1)*SIDE - 6, 15 + SIDE, text=f"{money}")


canvas.bind("<1>", click)

canvas.after(100, setup)
root.mainloop()
