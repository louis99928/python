from ttkbootstrap import *
import sys
import os
from tkinter import filedialog

os.chdir(sys.path[0])


def test():
    print("test")


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    label2.config(text=file_path)


def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


font_size = 20
window = tk.Tk()
window.title("my gui")
window.option_add("*font",
                  ("Helvetica", font_size))  #設定預設字型，這裡設為Helvetica, 大小是20

style = Style(theme="minty")  #設定主題
style.configure('my.TButton', font=('Helvetica', font_size))  # 設定按鈕字型

label = Label(window, text="選擇檔案:")  # stickt="E"=east 靠右對齊
label.grid(row=0, column=0, sticky="E")

label2 = Label(window, text="無")
label2.grid(row=0, column=1, sticky="E")  # stickt="E"=east 靠右對齊

bttton = Button(window, text="瀏覽", command=open_file,
                style="my.TButton")  #設定按鈕樣式
bttton.grid(row=0, column=2, sticky="E")

button2 = Button(window, text="顯示", command=show_image, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(window, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3, sticky="WNES")
window.mainloop()
