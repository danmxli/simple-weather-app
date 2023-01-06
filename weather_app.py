# import tkinter library
from tkinter import *

# create root window
root = Tk()
root.title('weather app testing gui')
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# entry
userEntry = Entry(root, width=20, borderwidth=3, font='Arial 12')
userEntry.pack()
temp_entry = Entry(root, width=20, borderwidth=3, font='Arial 12')
temp_entry.pack()


# variable of type string, initially set to first name
view_name = StringVar()
view_name.set("simple view")
# variable of type string, initially set to celcius
temp_unit = StringVar()
temp_unit.set("c")


# function
def clickButton(value):
    userEntry.delete(0, END)
    userEntry.insert(0, value)

# temp conversion function
def temp_conversion(unit):
    temp = temp_entry.get()
    temp_entry.delete(0, END)
    if unit == "c":
        temp = temp
    if unit == "f":
        # test conditional statement only
        temp = 0
    temp_entry.insert(0, temp)

# radiobutton
Radiobutton(root, text="my first name", variable=view_name, value="Dan").pack()
Radiobutton(root, text="my last name", variable=view_name, value="Li").pack()

Radiobutton(root, text="celcius", variable=temp_unit, value="c").pack()
Radiobutton(root, text="fahrenheit", variable=temp_unit, value="f").pack()


# button
buttonView = Button(root, text="select view", command=lambda: clickButton(view_name.get()))
buttonView.pack()

button_temp = Button(root, text="select unit", command=lambda: temp_conversion(temp_unit.get()))
button_temp.pack()

# run 
root.mainloop()
