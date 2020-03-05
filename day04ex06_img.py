from tkinter import Tk, PhotoImage, Label, Entry, Button

def change_img():
    path=entry.get()
    img=PhotoImage(file=path)
    imgLabel.configure({"image":img})
    imgLabel.image=img


win=Tk()

photo=PhotoImage(file="img01.gif")
imgLabel=Label(win, image=photo)
imgLabel.pack()

entry=Entry(win)
entry.pack()

btn=Button(win, text="사진교체", command=change_img)
btn.pack()

if __name__ =='__main__':
    win.mainloop()
