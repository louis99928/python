from ttkbootstrap import *
import sys
import os
from tkinter import filedialog


def test():
    print("test")


def show():
    entry_text = entry.get()
    n = eval(entry_text)
    label.config(text=n)


font_size = 20
window = tk.Tk()
window.title("my gui")
window.option_add("*font",
                  ("Helvetica", font_size))  #設定預設字型，這裡設為Helvetica, 大小是20

style = Style(theme="minty")  #設定主題
style.configure('my.TButton', font=('Helvetica', font_size))  # 設定按鈕字型

entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label = Label(window, text="計算結果:")
label.grid(row=2, column=0, columnspan=2, sticky="N")

bttton = Button(window, text="顯示計算結果", command=show,
                style="my.TButton")  #設定按鈕樣式
bttton.grid(row=1, column=0, columnspan=1, sticky="E")

window.mainloop()
