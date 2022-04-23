from tkinter import *
from main_page import command

win = Tk()
win.title("Master")
btn = Button(win, text= "Speak", width=10, height=3,bg="yellow", fg="black", command=command)
btn.place(x=650,y=500)
btn = Button(win,text="Close",width=10,height=3,bg="Green")
btn.place(x=725,y=500)
canvas =Canvas(width=500,height=500)
canvas.pack()
photo = PhotoImage(file='C:/Users/welcome/Downloads/Virtual Assistent/Virtual-Assistant-With-GUI-main/abcd.png')
canvas.create_image(200,200,image=photo,anchor=CENTER)
win.mainloop()