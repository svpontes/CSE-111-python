from tkinter import *

app=Tk()

app.title("Scene")
app.geometry("800x600")
app.configure(background="#008")

txt1=Label(app, text="Scene Def learning", background="#ff0" ,foreground="#000")
txt1.place(x=10,y=10, width=120, height=30)

app.mainloop()