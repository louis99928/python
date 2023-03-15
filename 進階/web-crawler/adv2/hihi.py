from tkinter import *
import sys
import os
from PIL import Image, ImageTk


def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(my_img2, 10, 0)
    elif key == "Left":
        canvas.move(my_img2, -10, 0)
    elif key == "Up":
        canvas.move(my_img2, 0, -10)
    elif key == "Down":
        canvas.move(my_img2, 0, 10)
    elif key == "d":
        canvas.move(my_img, 10, 0)
    elif key == "a":
        canvas.move(my_img, -10, 0)
    elif key == "w":
        canvas.move(my_img, 0, -10)
    elif key == "s":
        canvas.move(my_img, 0, 10)


def exit_fun():
    windows.destroy()


os.chdir(sys.path[0])
windows = Tk()
quit_button = Button(windows, text='quit', command=exit_fun)
quit_button.pack()
windows.title('my first GUI')
canvas = Canvas(windows, width=10000, height=10000)
canvas.pack()
windows.iconbitmap('crocodile2.ico')
img = PhotoImage(file='chicken1.png')
img2 = PhotoImage(file='chicken2.png')
img3 = PhotoImage(file='北七.png')

canvas.bind_all('<Key>', move_circle)

my_img = canvas.create_image(300, 600, image=img)
my_img2 = canvas.create_image(600, 300, image=img2)
my_img3 = canvas.create_image(600, 550, image=img3)
# circle=canvas.create_oval(250,150,300,200,fill='red')
# rect=canvas.create_rectangle(220,400,340,430,fill='red')
# msg = canvas.create_text(300,
#                          100,
#                          text='你看看這個北七',
#                          fill='black',
#                          font=('Arial,30'))

windows.mainloop()