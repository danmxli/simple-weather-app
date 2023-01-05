from tkinter import *
import requests
import json
from datetime import datetime

# root window
root = Tk()
root.config(bg="#3a3697", padx=10, pady=10)
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# get api key from https://openweathermap.org/

# api request function
def fetch():
    api_key = "4ae7fb8539618d265f7229f3d7431a45"
    city_name = userin_entry.get()
    userin_entry.delete(0, END)
    # request try and catch
    # api call from https://openweathermap.org/current
    try:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")
    except Exception as e:
        print("request error")
    # display json test
    userin_entry.insert(0, data.json())

# entry
userin_entry = Entry(root, width=20, borderwidth=10, font='arial 15')
userin_entry.pack()

# labels
userin_label = Label(root, text="Enter City")
userin_label.pack()

# buttons
fetch_btn = Button(root, text="Get Data", command=lambda : fetch())
fetch_btn.pack()

# run
root.mainloop()
