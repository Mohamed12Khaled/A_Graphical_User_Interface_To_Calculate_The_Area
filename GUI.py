from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("400x400")
root.title("area")

eh = Entry(root)
ew = Entry(root)

lh = Label(root, text="Height")
lw = Label(root, text="Width")
lr = Label(root, text="Result")

lh.place(x=100, y=20)
lw.place(x=100, y=60)
lr.place(x=100, y=90)
eh.place(x=150, y=20)
ew.place(x=150, y=60)

def calculate():
    h = float(eh.get())
    w = float(ew.get())
    area = h * w
    showinfo(title="Area", message=f"result = {area}")

res = Button(root, text="Calculate", command=calculate)
res.place(x=180, y=90)

root.mainloop()

