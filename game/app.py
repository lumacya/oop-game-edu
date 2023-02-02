from tkinter import *
import time

tk = Tk()

tk.title('OOP Education')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()

while not False:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
