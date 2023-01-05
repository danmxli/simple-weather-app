from tkinter import *
import requests
import json
from datetime import datetime

# root window
"""
root = Tk()
root.config(bg="#3a3697", padx=10, pady=10)

"""

# get api key from https://openweathermap.org/
api_key = "4ae7fb8539618d265f7229f3d7431a45"

fetch_city = input("enter city")

# request try and catch
# api call from https://openweathermap.org/current
try:
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={fetch_city}&units=imperial&APPID={api_key}")
except Exception as e:
    print("request error")

print(data.json())





# labels


# run
# root.mainloop()