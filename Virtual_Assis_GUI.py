from tkinter import *
from PIL import ImageTk, Image
from main_page import command

root = Tk()

root.title('🤖Virtual Assistant🤖')
root.geometry('800x300')

img = ImageTk.PhotoImage(Image.open('Virtual-Assistant-With-GUI-main/G.jpg'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')

userText = StringVar()

userText.set('Your Virtual Assistant')
userFrame = LabelFrame(root, text='CALIX', font=('Railways', 20, 'bold'))

userFrame.pack(fill='both', expand='yes')
top = Message(userFrame, textvariable=userText, bg='black', fg='white')
top.config(font=("Century Gothic", 30, 'bold'))
top.pack(side='top', fill='both', expand='yes')

btn = Button(root, text='Run', font=('railways',10,'bold'),bg='red', fg='white', command=command).pack(fill='x', expand='no')
btn2 = Button(root, text='Close', font=('railways',10,'bold'),bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')

root.mainloop()