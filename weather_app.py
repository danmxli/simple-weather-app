from tkinter import *
import requests
import json
from datetime import datetime

# root window
root = Tk()
root.config(bg="#3a3697", padx=10, pady=10)
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# get api key from https://openweathermap.org/
api_key = "4ae7fb8539618d265f7229f3d7431a45"



# run
root.mainloop()