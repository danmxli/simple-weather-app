# import
from tkinter import *
import sqlite3

root = Tk()
root.title("prototype weather database app")
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# create test database
conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE USER_INFO(
    v_code INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);''')

conn.close()

root.mainloop()