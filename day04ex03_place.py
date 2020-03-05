from tkinter import Tk
from tkinter.ttk import Button, Label, Entry

win=Tk()
btn1=Button(win, text="화씨->섭씨")
lbl1 = Label(win, text="화씨")
entry1=Entry(win)


lbl2 = Label(win, text="섭씨")
btn2=Button(win, text="섭씨->화씨")
entry2=Entry(win)

lbl1.place(x=0, y=0)
entry1.place(x=30, y=0)
btn1.place(x=180, y=0)

lbl2.place(x=0, y=30)
entry2.place(x=30, y=30)
btn2.place(x=180, y=30)

entry1.insert(0, 0)
entry2.insert(0, 0)

if __name__ == '__main__':
    win.mainloop()