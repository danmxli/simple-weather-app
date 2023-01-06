import tkinter
from tkinter import *
import requests
import json
from datetime import datetime
import sqlite3

# root window
root = Tk()
root.config(bg="#eee7d8", padx=10, pady=10)
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# get api key from https://openweathermap.org/

# global list to store requested data
global data_list


# hide entry text function
def hide_text(e):
    userin_entry.delete(0, END)


# unit conversion function
t_unit = StringVar()
t_unit.set("f")


def unit_conversion(f_temp, unit):
    c_temp = round(((f_temp - 32) * (5 / 9)), 2)
    if unit == "c":
        return c_temp
    if unit == "f":
        return f_temp
    return f_temp


# view simple or detail
view_type = StringVar()
view_type.set("s")


# api request function
def fetch(type):
    global data_list
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

    # define variables
    timestamp = str(datetime.now())
    lon = (data['coord']['lon'])
    lat = (data['coord']['lat'])
    weather_dsc = data['weather'][0]['description']
    temperature = unit_conversion(data['main']['temp'], t_unit.get())
    feels_like = unit_conversion(data['main']['feels_like'], t_unit.get())
    temp_min = unit_conversion(data['main']['temp_min'], t_unit.get())
    temp_max = unit_conversion(data['main']['temp_max'], t_unit.get())
    humidity = int(data['main']['humidity'])
    wind_speed = (data['wind']['speed'])
    wind_direction = int(data['wind']['deg'])
    of_country = data['sys']['country']

    # update list
    data_list = [
        timestamp,
        lon,
        lat,
        weather_dsc,
        temperature,
        feels_like,
        temp_min,
        temp_max,
        humidity,
        wind_speed,
        wind_direction,
        of_country
    ]

    # insert display
    print_unit = ""
    if t_unit.get() == "c":
        print_unit = " celcius"
    if t_unit.get() == "f":
        print_unit = " fahrenheit"

    display_w_info.delete("1.0", tkinter.END)
    display_w_info.insert("1.0", "data retreived " + timestamp + "\n")
    if type == "s":
        display_w_info.insert("2.0", "now: " + weather_dsc + "\n")
        display_w_info.insert("3.0", "temperature: " + str(temperature) + print_unit + "\n")
    if type == "d":
        display_w_info.insert("2.0", "country: " + of_country + "\n")
        display_w_info.insert("3.0", "longitude: " + str(lon) + "\n")
        display_w_info.insert("4.0", "latitude: " + str(lat) + "\n")
        display_w_info.insert("5.0", "now: " + weather_dsc + "\n")

        display_w_info.insert("6.0", "temperature: " + str(temperature) + print_unit + "\n")
        display_w_info.insert("7.0", "feels like: " + str(feels_like) + print_unit + "\n")
        display_w_info.insert("8.0", "min. temperature: " + str(temp_min) + print_unit + "\n")
        display_w_info.insert("9.0", "max. temperature: " + str(temp_max) + print_unit + "\n")

        display_w_info.insert("10.0", "humidity: " + str(humidity) + "\n")
        display_w_info.insert("11.0", "wind speed: " + str(wind_speed) + " m/s\n")
        display_w_info.insert("12.0", "wind direction: " + str(wind_direction))


'''
c.execute(""" 
        CREATE TABLE weather_data (
               t_timestamp text, 
               t_lon real,
               t_lat real,
               t_weather_dsc text,
               t_temperature real,
               t_feels_like real, 
               t_temp_min real,
               t_temp_max real,
               t_humidity integer,
               t_wind_speed real,
               t_wind_direction integer,
               t_country text
        )""")
'''


# insert to database function
def submit():
    global data_list
    # connect to database
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    # insert
    c.execute("""INSERT INTO weather_data VALUES(
        :t_timestamp, 
        :t_lon,
        :t_lat,
        :t_weather_dsc,
        :t_temperature,
        :t_feels_like, 
        :t_temp_min,
        :t_temp_max,
        :t_humidity,
        :t_wind_speed,
        :t_wind_direction,
        :t_country
        )""",
              {
                  't_timestamp': data_list[0],
                  't_lon': data_list[1],
                  't_lat': data_list[2],
                  't_weather_dsc': data_list[3],
                  't_temperature': data_list[4],
                  't_feels_like': data_list[5],
                  't_temp_min': data_list[6],
                  't_temp_max': data_list[7],
                  't_humidity': data_list[8],
                  't_wind_speed': data_list[9],
                  't_wind_direction': data_list[10],
                  't_country': data_list[11]
              }
              )
    display_w_info.delete("1.0", tkinter.END)
    display_w_info.insert("1.0", "successfully inserted to database.")
    conn.commit()
    conn.close()


# query all function
def q_all():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    # all
    c.execute("SELECT *, oid FROM weather_data")
    log = c.fetchall()
    index = 0
    print_log = ""
    for log in log:
        for index in range(12):
            print_log += str(log[index]) + " "
        print_log += "\n"

    print('querying...')
    print(print_log)
    conn.commit()
    conn.close()
    return


# open new window function
def open_db_window():
    db_window = Toplevel(root)
    db_window.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\db_icon.ico")
    db_window.config(padx=200, pady=10)
    Button(db_window, text="select all", command=lambda: q_all()).pack()


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
addto_database_btn = Button(root, text="Add to Database", borderwidth=5, command=lambda: submit())
addto_database_btn.grid(row=4, column=0, pady=5)
# open database window
open_window_btn = Button(root, text="Open Database", borderwidth=5, command=open_db_window)
open_window_btn.grid(row=5, column=0, pady=5)

# radiobutton
Radiobutton(root, text="fahrenheit", variable=t_unit, value="f").grid(row=0, column=5)
Radiobutton(root, text="celcius", variable=t_unit, value="c").grid(row=1, column=5)

Radiobutton(root, text="simple view", variable=view_type, value="s").grid(row=4, column=5, pady=5)
Radiobutton(root, text="detailed view", variable=view_type, value="d").grid(row=5, column=5, pady=5)

# run
root.mainloop()
