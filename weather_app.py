# import
from tkinter import *
import sqlite3

root = Tk()
root.title("prototype weather database app")
root.iconbitmap(r"C:\Users\danmu\my_projects\simple-weather-app\weather_images\wapp_icon.ico")

'''
c.execute("""CREATE TABLE userinfo (first_name TEXT NOT NULL, last_name TEXT NOT NULL, vcode INT NOT NULL)""")
''' 

# update function
def submit():
    # connect test database
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    # insert
    c.execute("""INSERT INTO userinfo VALUES(
        :f_name, :l_name, :vcode
        )""",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'vcode': code.get()
    }
    )

    conn.commit()
    conn.close()

    # delete typed data
    code.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)

# entry 
code = Entry(root, width=20)
code.grid(row=0, column=1)
f_name = Entry(root, width=20)
f_name.grid(row=1, column=1)
l_name = Entry(root, width=20)
l_name.grid(row=2, column=1)

# label
code_label = Label(root, text="verification code").grid(row=0, column=0)
f_name_label = Label(root, text="first name").grid(row=1, column=0)
l_name_label = Label(root, text="last name").grid(row=2, column=0)

# update button
update_btn = Button(root, text="add to database", command=lambda: submit())
update_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()