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


# unit conversion function
t_unit = StringVar()
t_unit.set("f")
def unit_conversion(f_temp, unit):
    c_temp = round(((f_temp - 32) * (5 / 9)), 2)
    temp_str = ""
    if unit == "c":
        temp_str = str(c_temp) + " celcius"
    if unit == "f":
        temp_str = str(f_temp) + " fahrenheit"
    return temp_str


# view simple or detail
view_type = StringVar()
view_type.set("s")

# api request function
def fetch(type):
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
    timestamp = str(datetime.now())
    lon = str(data['coord']['lon'])
    lat = str(data['coord']['lat'])
    weather_dsc = data['weather'][0]['description']
    temperature = unit_conversion(data['main']['temp'], t_unit.get())
    feels_like = unit_conversion(data['main']['feels_like'], t_unit.get())
    temp_min = unit_conversion(data['main']['temp_min'], t_unit.get())
    temp_max = unit_conversion(data['main']['temp_max'], t_unit.get())
    humidity = str(data['main']['humidity'])
    wind_speed = str(data['wind']['speed'])
    wind_direction = str(data['wind']['deg'])
    of_country = data['sys']['country']

    # insert display
    display_w_info.delete("1.0", tkinter.END)
    display_w_info.insert("1.0", "data retreived " + timestamp + "\n")
    if type == "s":
        display_w_info.insert("2.0", "now: " + weather_dsc + "\n")
        display_w_info.insert("3.0", "temperature: " + temperature + "\n")
    if type == "d":
        display_w_info.insert("2.0", "country: " + of_country + "\n")
        display_w_info.insert("3.0", "longitude: " + lon + "\n")
        display_w_info.insert("4.0", "latitude: " + lat + "\n")
        display_w_info.insert("5.0", "now: " + weather_dsc + "\n")
        display_w_info.insert("6.0", "temperature: " + temperature + "\n")
        display_w_info.insert("7.0", "feels like: " + feels_like + "\n")
        display_w_info.insert("8.0", "min. temperature: " + temp_min + "\n")
        display_w_info.insert("9.0", "max. temperature: " + temp_max + "\n")
        display_w_info.insert("10.0", "humidity: " + humidity + "\n")
        display_w_info.insert("11.0", "wind speed: " + wind_speed + " m/s\n")
        display_w_info.insert("12.0", "wind direction: " + wind_direction)



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
fetch_btn = Button(root, text="Get Data", borderwidth=5, command=lambda: fetch(view_type.get()))
fetch_btn.grid(row=2, column=0)
# add to database
addto_database_btn = Button(root, text="Add to Database", borderwidth=5)
addto_database_btn.grid(row=4, column=0, pady=5)
# access database
open_database_btn = Button(root, text="Open Database", borderwidth=5, command=open_db_window)
open_database_btn.grid(row=5, column=0, pady=5)

"""/// IN DEVELOPMENT ///"""
# radiobutton
Radiobutton(root, text="fahrenheit", variable=t_unit, value="f").grid(row=0, column=5)
Radiobutton(root, text="celcius", variable=t_unit, value="c").grid(row=1, column=5)

Radiobutton(root, text="simple view", variable=view_type, value="s").grid(row=4, column=5, pady=5)
Radiobutton(root, text="detailed view", variable=view_type, value="d").grid(row=5, column=5,pady=5)

# run
root.mainloop()
