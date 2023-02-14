from tkinter import *
import time

tk = Tk()

tk.title('OOP Education')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()

class Ball:

    def __init__(self, canvas, color, x, y, up, down, left, right):
        self.__canvas = canvas
        self.__x = 0
        self.__y = 0
        self.__id = canvas.create_oval(10,10, 25, 25, fill=color)
        # self.__canvas.move(self.id, x, y)
        # self.__canvas.bind_all(right, self.turn_right)
        # self.__canvas.bind_all(left, self.turn_left)
        # self.__canvas.bind_all(up, self.turn_up)
        # self.__canvas.bind_all(down, self.turn_down)
        self.__canvas_height = self.__canvas.winfo_height()
        self.__canvas_width = self.__canvas.winfo_width()

    def __turn_right(self, event):
        # pos = self.__canvas.coords(self.__id)
        # if not pos[2] >= self.__canvas_width:
        #     self.__x = 2
        #     self.__y = 0
        pass

    def __turn_left(self, event):
        # pos = self.__canvas.coords(self.__id)
        # if not pos[0] <= 0:
        #     self.__x = -2
        #     self.__y = 0
        pass


    def __turn_up(self, event):
        # pos = self.__canvas.coords(self.__id)
        # if not pos[1] <= 0:
        #     self.__x = 0
        #     self.__y = -2
        pass


    def __turn_down(self, event):
        # pos = self.__canvas.coords(self.__id)
        # if not pos[3] >= self.__canvas_height:
        #     self.__x = 0
        #     self.__y = 2
        pass

    def draw(self):
        # self.__canvas.move(self.__id, self.__x, self.__y)
        # pos = self.__canvas.coords(self.__id)

        # if pos[0] <= 0:
        #     self.__x = 0
        # if pos[1] <= 0:
        #     self.__y = 0
        # if pos[2] == self.__canvas_width:
        #     self.__x = 0
        # if pos[3] == self.canvas_height:
        #     self.__y = 0
        pass

ball_one = Ball(canvas, 'red', 150, 150, '<w>', '<s>', '<a>', '<d>')

while not False:
    ball_one.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
