import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
import os
import sys
import datetime
import requests

os.chdir(sys.path[0])


def on_closing():
    window.destroy()
    plt.close('all')


def draw_graph():
    api_key = "892da2f13edf3c7f382637760e72d224"  #API key

    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    lon = "121.5319"  #taipei 的經度
    lat = '25.0478'  #taipei 的緯度
    exclude = 'minutely,houly'
    units = "metric"
    lang = 'zh_tw'

    send_url = base_url
    send_url += 'lat=' + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += '&units=' + units
    send_url += '&lang=' + lang
    print(send_url)
    response = requests.get(send_url)
    info = response.json()

    day = []
    temp2 = []
    if 'daily' in info.keys():
        for i in range(7):
            temp = info['daily'][i]['temp']['day']
            time = datetime.datetime.fromtimestamp(
                info['daily'][i]['dt']).strftime('%m/%d')
            # print(f"{time}的溫度是{temp}度")
            day.append(time)
            temp2.append(temp)
    else:
        print("request fail")

    font = FontProperties(fname='NotoSansTC-Black.otf', size=14)
    fig, ax = plt.subplots()
    ax.plot(day, temp2)
    ax.set_xlabel('7 天氣溫', fontproperties=font)
    ax.set_ylabel('溫度(C)', fontproperties=font)
    ax.set_title('日期', fontproperties=font)

    cnavas = FigureCanvasTkAgg(fig, master=window)
    cnavas.draw()
    cnavas = cnavas.get_tk_widget()
    cnavas.grid(row=0, column=0, padx=10, pady=10)


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")

draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()
