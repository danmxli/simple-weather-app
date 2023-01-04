# import tkinter library
from tkinter import *

# create root window
root = Tk()
root.title('weather app testing gui')

# custom icon
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

# frame
main_frame = Frame(root, bg="#6eeac1", height=10, width=50)
main_frame.pack()

# entry
userEntry = Entry(root, width=40, borderwidth=6, font=('Arial 12'))
userEntry.pack()

# list text and mode
list_values = [
    ("simple view", "this is the simple view"),
    ("detailed view", "this is the detailed view. Will update the gui later."),
]
view_s = StringVar()
view_s.set("simple view") 

# for loop to pack radio button on root
for text, mode in list_values:
    Radiobutton(root, text=text, variable=view_s, value=mode).pack()

# function 
def clickButton(value):
    userEntry.delete(0, END)
    userEntry.insert(0, value)

# Radiobutton(root, text="Condition one", variable=num, value=1, command=lambda: clickButton(num.get())).pack()
# Radiobutton(root, text="Condition two", variable=num, value=2, command=lambda: clickButton(num.get())).pack()

buttonView = Button(root, text="select view", command=lambda: clickButton(view_s.get()))
buttonView.pack()

# run 
root.mainloop()