import tkinter
from tkinter import *
import requests
import json
from datetime import datetime

# root window
root = Tk()
root.config(bg="#eee7d8", padx=10, pady=10)
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")


# get api key from https://openweathermap.org/

# hide entry text function
def hide_text(e):
    userin_entry.delete(0, END)

"""/// IN DEVELOPMENT ///"""
# unit conversion
t_unit = StringVar()
t_unit.set("f")

# unit conversion function
def unit_conversion(f_temp, unit):
    c_temp = round(((f_temp - 32) * (5 / 9)), 2)
    temp_str = ""
    if unit == "c":
        temp_str = str(c_temp) + " celcius"
    if unit == "f":
        temp_str = str(f_temp) + " fahrenheit"
    return temp_str


# api request function
def fetch():
    api_key = "4ae7fb8539618d265f7229f3d7431a45"
    city_name = userin_entry.get()

    # request try and catch
    # api call from https://openweathermap.org/current
    try:
        data_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")
        data = json.loads(data_request.content)
    except Exception as e:
        print("error")

    if data['cod'] != 200:
        display_w_info.delete("1.0", tkinter.END)
        display_w_info.insert("1.0", "please enter a valid city")
        return

    # define str variables
    lon = str(data['coord']['lon'])
    lat = str(data['coord']['lat'])
    weather_dsc = data['weather'][0]['description']
    temperature = unit_conversion(data['main']['temp'], t_unit.get())
    feels_like = str(data['main']['feels_like'])
    temp_min = str(data['main']['temp_min'])
    temp_max = str(data['main']['temp_max'])
    humidity = str(data['main']['humidity'])
    wind_speed = str(data['wind']['speed'])
    wind_direction = str(data['wind']['deg'])
    of_country = data['sys']['country']

    # insert display
    display_w_info.delete("1.0", tkinter.END)
    display_w_info.insert("1.0", "longitude: " + lon + "\n")
    display_w_info.insert("2.0", "latitude: " + lat + "\n")
    display_w_info.insert("3.0", weather_dsc + "\n")
    display_w_info.insert("4.0", "temperature: " + temperature + "\n")
    display_w_info.insert("5.0", "")
    display_w_info.insert("6.0", "")
    display_w_info.insert("7.0", "")
    display_w_info.insert("8.0", "")
    display_w_info.insert("9.0", "")
    display_w_info.insert("10.0", "")
    display_w_info.insert("11.0", "")


# open new window function
def open_db_window():
    db_window = Toplevel(root)
    db_window.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\db_icon.ico")


# display
display_w_info = Text(root, width=50, height=20)
display_w_info.grid(row=3, column=0)

# entry
userin_entry = Entry(root, width=20, borderwidth=10, font='arial 15')
userin_entry.insert(0, "Enter Name of City")
userin_entry.bind("<FocusIn>", hide_text)
userin_entry.grid(row=1, column=0, padx=100)

# buttons
fetch_btn = Button(root, text="Get Data", borderwidth=5, command=lambda: fetch())
fetch_btn.grid(row=2, column=0)
# button to access database
open_database_btn = Button(root, text="Open Database", borderwidth=5, command=open_db_window)
open_database_btn.grid(row=4, column=0)

"""/// IN DEVELOPMENT ///"""
# radiobutton
Radiobutton(root, text="fahrenheit", variable=t_unit, value="f").grid(row=0, column=5)
Radiobutton(root, text="celcius", variable=t_unit, value="c").grid(row=1, column=5)

Radiobutton(root, text="simple view").grid(row=4, column=5, pady=5)
Radiobutton(root, text="detailed view").grid(row=5, column=5,pady=5)

# run
root.mainloop()
