# import
from tkinter import *
import sqlite3

root = Tk()
root.title("prototype weather database app")
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# create and connect to database
main_db = sqlite3.connect('verification_codes.db')

# create cursor
cursor = main_db.cursor()

# commit changes
main_db.commit()

# close connection
main_db.close()

root.mainloop()