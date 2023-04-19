from ttkbootstrap import *
import sys
import os
from tkinter import filedialog

font_size = 20
window = tk.Tk()
window.title("my gui")
window.option_add("*font",
                  ("Helvetica", font_size))  #設定預設字型，這裡設為Helvetica, 大小是20

check_type = BooleanVar()
check_type.set(True)

check_label = Label(window, text="True")
check_label.grid(row=1, column=2)


def on_switch_change():
    n = False
    check_label.config(text=n)


check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)

check.grid(row=1, column=1)

window.mainloop()
