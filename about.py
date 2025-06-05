from tkinter import *
import os
from PIL import ImageTk, Image
import customtkinter

root = Tk()
root.geometry('1366x768')
root.title("Login")

# Canvas for background image
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('b5.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1, 1, anchor=NW, image=photo)

# Button functions
def on_click1():
    root.destroy()
    os.system("python about.py")

def on_click2():
    root.destroy()
    os.system("python services.py")

def on_click3():
    root.destroy()
    os.system("python notebook.py")

def on_click4():
    root.destroy()
    os.system("python main.py")

# Common button style
button_style = {
    "master": root,
    "corner_radius": 0,          # Make it rectangular
    "hover_color": "#0b84f3",
    "fg_color": "#1f6aa5",
    "text_color": "white",
    "width": 140,
    "height": 40
}

# Creating rectangular buttons
button1 = customtkinter.CTkButton(text="About Us", command=on_click1, **button_style)
button1.place(x=480, y=20)

button2 = customtkinter.CTkButton(text="Services", command=on_click2, **button_style)
button2.place(x=640, y=20)

button3 = customtkinter.CTkButton(text="Generate Report", command=on_click3, **button_style)
button3.place(x=800, y=20)

button4 = customtkinter.CTkButton(text="Logout", command=on_click4, **button_style)
button4.place(x=1010, y=20)

root.mainloop()
