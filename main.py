import os
from tkinter import *
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("light")  # or "dark"
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("NLP")
app.geometry("1366x768")
# Use zoomed window with title bar (instead of fullscreen)
app.state('zoomed')  # Maximized with minimize/maximize/close buttons

def on_click1():
    app.destroy()
    os.system("python about.py")

def on_click2():
    app.destroy()
    os.system("python services.py")

def on_click3():
    app.destroy()
    os.system("python notebook.py")

def on_click4():
    app.destroy()

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path)
            img.thumbnail((1366, 768))  # Resize for display
            images.append(ImageTk.PhotoImage(img))
    return images

def show_scrollable_images(folder_path):
    canvas = Canvas(app)
    scrollbar = Scrollbar(app, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = Frame(canvas)
    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    images = load_images_from_folder(folder_path)
    for img in images:
        label = Label(scroll_frame, image=img)
        label.image = img  # Prevent garbage collection
        label.pack(pady=0)

# 🔧 Change this to your folder containing images
show_scrollable_images("img")

# Buttons
button = customtkinter.CTkButton(
    master=app,
    text="About Us",
    corner_radius=15,
    hover_color="violet",
    fg_color="purple",
    height=50,
    font=("Georgio", 14),
    command=on_click1
)
button.place(x=500, y=20)

button = customtkinter.CTkButton(
    master=app,
    text="Services",
    corner_radius=15,
    hover_color="violet",
    fg_color="purple",
    height=50,
    font=("Georgio", 14),
    command=on_click2
)
button.place(x=650, y=20)

button = customtkinter.CTkButton(
    master=app,
    text="Generate Report",
    corner_radius=15,
    hover_color="violet",
    fg_color="purple",
    height=50,
    font=("Georgio", 14),
    command=on_click3
)
button.place(x=800, y=20)

button = customtkinter.CTkButton(
    master=app,
    text="Logout",
    corner_radius=15,
    hover_color="violet",
    fg_color="purple",
    height=50,
    font=("Georgio", 14),
    command=on_click4
)
button.place(x=950, y=20)

app.mainloop()
