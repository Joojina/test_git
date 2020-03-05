from tkinter import Tk, Canvas, Button
import time

myColor="blue"

point=[]

def paint(event):
    x,y = event.x-1, event.y-1
    x2,y2 = x+1, y+1
    point.append((x,y,x2,y2))

    # canvas.create_oval(x,y,x2,y2, fill=myColor, outline=myColor)
    canvas.create_rectangle(x, y, x2, y2, fill=myColor, outline=myColor)


def change_color():
    global myColor
    myColor="red"

win=Tk()
canvas=Canvas(win)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

btn=Button(win, text="빨간색", command=change_color)
btn.pack()


if __name__ == '__main__':
    win.mainloop()