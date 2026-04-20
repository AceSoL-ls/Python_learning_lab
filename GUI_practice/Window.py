from tkinter import *

window = Tk()

label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)
label.pack()

window.mainloop()