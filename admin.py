from tkinter import *
from tkinter import messagebox
import ast
import matplotlib.pyplot as plt
import numpy as np
import pymysql

admin = Tk()
admin.title('ADMIN PAGE')
admin.geometry('925x500+300+200')
admin.configure(bg="#282634")
admin.resizable(False, False)

def sales():
    messagebox.showinfo('REDIRECTING','TO THE SALES GRAPH SECTION')
    admin.destroy()
    import graph



def bill():
    messagebox.showinfo('REDIRECTING','TO THE BILL AREA')
    admin.destroy()
    import billing


def register():
    messagebox.showinfo('REDIRECTING','TO CUSTOMER FORM')
    admin.destroy()
    import registration












img = PhotoImage(file='mainimg.png')
Label(admin, image=img, border=0, width=400, height=400, bg='#78290F').place(x=50, y=50)

frame = Frame(admin, width=350, height=350, bg="#282634")
frame.place(x=480, y=70)

heading = Label(frame, text='SERVICES', fg='#ffecd1', bg='#282634', font=('Georgia', 23, 'bold'))
heading.place(x=120, y=5)


Button(frame, width=20, pady=7, text='SALES', font=('Georgia'), bg='#f44459', fg='#ffecd1', border=0,command=sales
      ).place(x=75, y=70)

Button(frame, width=20, pady=7, text='BILLING', font=('Georgia'), bg='#f44459', fg='#ffecd1', border=0,
       command=bill).place(x=75, y=140)

Button(frame, width=20, pady=7, text='REGISTRATION', font=('Georgia'), bg='#f44459', fg='#ffecd1', border=0,command=register
      ).place(x=75, y=210)

Button(frame, width=20, pady=7, text='LOG OUT', font=('Georgia'), bg='#f44459', fg='#ffecd1', border=0,command=admin.destroy
      ).place(x=75, y=280)











admin.mainloop()
