from tkinter import *


def hi_fun():
    global change
    print('hello lol')
    if change == False:
        display.config(text="hi lol", fg='red', bg='#74AEFA')
    else:
        display.config(text="hi lol", fg='#74AEFA', bg='red')
    change = not (change)


change = False
win = Tk()  #物件
win.title("lol")

#標籤文字   字顏色     背景顏色
display = Label(win, text="hi", fg='red', bg='#74AEFA')
display.pack()

#執行視窗   按鈕上文字         代執行文字
btn = Button(win, text="click me", command=hi_fun, fg='#29FF7B', bg='#74AEFA')
btn.pack()

#display.config(text="hi lol", fg='red', bg='#74AEFA')

win.mainloop()  #持續出現
