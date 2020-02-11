from tkinter import *
import random

GRID_SIZE = 8
CELL_SIZE = 50
MINES_COUNT = 10

go = 0
mines=set(random.sample(range(1, GRID_SIZE**2+1), MINES_COUNT))
clicked=set()
def gameover():
    for i in range(GRID_SIZE ** 2):
        if i in mines:
            c.itemconfig(i, fill="red")
        c.update()
        global go
        go = 1
def check_mines_near(data):
    return len(mines.intersection(data))
def generate_near_ids(id):
    if id == 1:
        data = {GRID_SIZE+1,2,GRID_SIZE+2}
    elif id == GRID_SIZE:
        data = {GRID_SIZE-1,GRID_SIZE*2,GRID_SIZE*2-1}
    elif id == GRID_SIZE**2:
        data = {id-GRID_SIZE,id-1,id-GRID_SIZE-1}
    elif id == GRID_SIZE**2-GRID_SIZE+1:
        data = {id+1,id-GRID_SIZE,id-GRID_SIZE+1}
    elif id < GRID_SIZE:
        data = {id+1,id-1,id+GRID_SIZE,id+GRID_SIZE-1,id+GRID_SIZE+1}
    elif id > GRID_SIZE**2-GRID_SIZE:
        data = {id+1,id-1,id-GRID_SIZE,id-GRID_SIZE-1,id-GRID_SIZE+1}
    elif id % GRID_SIZE == 1:
        data = {id+GRID_SIZE,id-GRID_SIZE,id+1,id+GRID_SIZE+1,id-GRID_SIZE+1}
    elif id % GRID_SIZE == 0:
        data = {id+GRID_SIZE,id-GRID_SIZE,id-1,id+GRID_SIZE-1,id-GRID_SIZE-1}
    else:
        data = {id-1,id+1,id-GRID_SIZE,id+GRID_SIZE,id-GRID_SIZE-1,id-GRID_SIZE+1,id+GRID_SIZE+1,id+GRID_SIZE-1}
    return data
def click(event):
    id = c.find_withtag(CURRENT)[0]
    if id in mines:
        gameover()
    elif id not in clicked and go == 0:
        c.itemconfig(CURRENT, fill="white")
        rec(id)
        c.update()
def mark(event):
    if go == 0:
        id = c.find_withtag(CURRENT)[0]
        if id not in clicked:
            clicked.add(id)
            x1, y1, x2, y2 = c.coords(id)
            c.itemconfig(CURRENT, fill="yellow")
        else:
            clicked.remove(id)
            c.itemconfig(CURRENT, fill="gray")
def rec(id):
      clicked.add(id)
      near = generate_near_ids(id)
      mines_arround = check_mines_near(near)
      if mines_arround:
        x1, y1, x2, y2 = c.coords(id)
        c.itemconfig(id, fill="white")
        c.create_text(x1+CELL_SIZE/2, y1+CELL_SIZE/2,
                    text=str(mines_arround), font="Arial {}".format(int(CELL_SIZE / 2)), fill='blue')
      else:
        for item in set(near).difference(clicked):
          c.itemconfig(item, fill="white")
          rec(item)

main_window = Tk()
main_window.title("Minesweep.py")
c = Canvas(main_window, width=GRID_SIZE * CELL_SIZE,height = GRID_SIZE * CELL_SIZE, bg = 'white')
c.pack()

c.bind("<Button-1>", click)
c.bind("<Button-2>", mark)

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        c.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,
                           i * CELL_SIZE + CELL_SIZE,
                           j * CELL_SIZE + CELL_SIZE, fill='gray')

main_window.mainloop()
