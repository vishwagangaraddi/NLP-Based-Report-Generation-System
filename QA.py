import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from docx import Document
from PIL import Image, ImageTk
import customtkinter
from docx import Document
from transformers import pipeline
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
customtkinter.set_appearance_mode("light")  # or "dark"
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("NLP")
#app.geometry("1366x768")
app.attributes('-fullscreen', True)
canv = Canvas(app, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back2.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
A=StringVar()
Q=StringVar()
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
# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering")

def on_click6():
    def answer_question(summary_text, user_question):

        try:
            result = qa_pipeline(question=user_question, context=summary_text)
            return result['answer']
        except Exception as e:
            return f"Error during QA: {e}"
    summary= text_widget.get("1.0", tk.END)
    q1=Q.get()
    answer = answer_question(summary, q1)
    A.set(answer)
    print("Answer:", answer)
def on_click5():
    filename = askopenfilename(filetypes=[("Docfiles", "*.*")])
    doc = Document(filename)
    text = ""
    for para in doc.paragraphs:
        if para.text.strip():
            text += para.text + "\n"
    summary = text
    print(summary)
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, summary)

button = customtkinter.CTkButton(
    master=app,
    text="Open File",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click5
)
button.place(x=350,y=100)

button = customtkinter.CTkButton(
    master=app,
    text="About Us",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click1
)
button.place(x=500,y=100)
button = customtkinter.CTkButton(
    master=app,
    text="Services",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click2
)
button.place(x=650,y=100)
button = customtkinter.CTkButton(
    master=app,
    text="Generate Report",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click3
)
button.place(x=800,y=100)
button = customtkinter.CTkButton(
    master=app,
    text="Logout",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click4
)
button.place(x=950,y=100)

button = customtkinter.CTkButton(
    master=app,
    text="Display Answer",
    corner_radius=10,          # Rounded corners
    hover_color="#0b84f3",     # Hover background color
    fg_color="#1f6aa5",        # Normal background color
    command=on_click6
)
button.place(x=850,y=350)
text_widget = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=10, font=("Georgio", 10))
text_widget.place(x=400,y=150)
l1=Label(app,text="Enter Your Question" , font=("Georgio", 12))
l1.place(x=400,y=350)
t1=Entry(app,textvar=Q, font=("Georgio", 12))
t1.place(x=600,y=350)
l2=Label(app,text="Answer", font=("Georgio", 12))
l2.place(x=400,y=400)
t1=Entry(app,textvar=A, width=60,font=("Georgio", 12))
t1.place(x=600,y=400)
app.mainloop()
