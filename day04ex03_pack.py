from tkinter import Tk
from tkinter.ttk import Button, Label, Entry

win=Tk()
btn1=Button(win, text="화씨->섭씨")
lbl1 = Label(win, text="화씨")
entry1=Entry(win)


lbl2 = Label(win, text="섭씨")
btn2=Button(win, text="섭씨->화씨")
entry2=Entry(win)

lbl1.pack()
entry1.pack()
btn1.pack()

lbl2.pack()
entry2.pack()
btn1.pack()

entry1.insert(0, 0)
entry2.insert(0, 0)

if __name__ == '__main__':
    win.mainloop()