from tkinter import *
#import graph1
import matplotlib.pyplot as plt
import numpy as np

win=Tk()
win.title('Sales Graph')
win.geometry('925x500+300+200')
win.configure(bg='#282633')
win.resizable(False,False)

def clear():
    jan.delete(0, END)
    feb.delete(0, END)
    mar.delete(0, END)
    apr.delete(0, END)
    may.delete(0, END)
    jun.delete(0, END)
    jul.delete(0, END)
    aug.delete(0, END)
    sep.delete(0, END)
    octo.delete(0, END)
    nov.delete(0, END)
    dec.delete(0, END)
    jan.insert(0, 'January')
    feb.insert(0, 'February')
    mar.insert(0, 'March')
    apr.insert(0, 'April')
    may.insert(0, 'May')
    jun.insert(0, 'June')
    jul.insert(0, 'July')
    aug.insert(0, 'August')
    sep.insert(0, 'September')
    octo.insert(0, 'October')
    nov.insert(0, 'November')
    dec.insert(0, 'December')

def graphing():
    x = np.array(
        ["1ST MONTH", "2ND MONTH", "3RD MONTH", "4TH MONTH", "5TH MONTH", "6TH MONTH", "7TH MONTH", "8TH MONTH",
         "9TH MONTH", "10TH MONTH", "11TH MONTH", "12TH MONTH"])
    y = np.array([int(jan.get()), int(feb.get()), int(mar.get()), int(apr.get()), int(may.get()), int(jun.get()),
                  int(jul.get()), int(aug.get()), int(sep.get()), int(octo.get()), int(nov.get()), int(dec.get())])
    a = max(y) + 9
    y_pos = np.arange(len(x))
    plt.xticks(y_pos, x, rotation=45, fontsize=5)
    plt.yticks(np.arange(0, a, 10))
    plt.xlabel("MONTHS")
    plt.ylabel("SALES IN RUPEES")
    plt.title("MONTHLY SALES")
    bars = plt.bar(x, y, color="#EB525D")

    for bar in bars:
        height = bar.get_height()
        text = f'{height}'
        label_x = bar.get_x() + bar.get_width() / 2
        label_y = bar.get_y() + height
        plt.text(label_x, label_y, text, ha='center')

    plt.show()
    clear()
def reset():
    jan.delete(0, END)
    feb.delete(0, END)
    mar.delete(0, END)
    apr.delete(0, END)
    may.delete(0, END)
    jun.delete(0, END)
    jul.delete(0, END)
    aug.delete(0, END)
    sep.delete(0, END)
    octo.delete(0, END)
    nov.delete(0, END)
    dec.delete(0, END)

img= PhotoImage(file="img.png")
Label(win,image=img,border=0,bg='#282633').place(x=10,y=90)

frame=Frame(win,width=350,height=390,bg='#282633')
frame.place(x=480,y=50)

heading=Label(frame,text='SALES',fg="#ffecd1",bg='#282634',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=20,y=5)

Frame(frame,width=295,height=2,bg='white').place(x=25,y=57)
#####---------------------
def on_enter(e):
    jan.delete(0,'end')
def on_leave(e):
    if jan.get()=='':
        jan.insert(0,'January')
jan = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
jan.place(x=25,y=80)
jan.insert(0,'January')
jan.bind("<FocusIn>",on_enter)
jan.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    feb.delete(0,'end')
def on_leave(e):
    if feb.get()=='':
        feb.insert(0,'February')
feb = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
feb.place(x=105,y=80)
feb.insert(0,'February')
feb.bind("<FocusIn>",on_enter)
feb.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    mar.delete(0,'end')
def on_leave(e):
    if mar.get()=='':
        mar.insert(0,'March')
mar = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
mar.place(x=195,y=80)
mar.insert(0,'March')
mar.bind("<FocusIn>",on_enter)
mar.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    apr.delete(0,'end')
def on_leave(e):
    if apr.get()=='':
        apr.insert(0,'April')
apr = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
apr.place(x=25,y=150)
apr.insert(0,'April')
apr.bind("<FocusIn>",on_enter)
apr.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    may.delete(0,'end')
def on_leave(e):
    if may.get()=='':
        may.insert(0,'May')
may = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
may.place(x=105,y=150)
may.insert(0,'May')
may.bind("<FocusIn>",on_enter)
may.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    jun.delete(0,'end')
def on_leave(e):
    if jun.get()=='':
        jun.insert(0,'June')
jun = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
jun.place(x=195,y=150)
jun.insert(0,'June')
jun.bind("<FocusIn>",on_enter)
jun.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    jul.delete(0,'end')
def on_leave(e):
    if jul.get()=='':
        jul.insert(0,'July')
jul = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
jul.place(x=25,y=220)
jul.insert(0,'July')
jul.bind("<FocusIn>",on_enter)
jul.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    aug.delete(0,'end')
def on_leave(e):
    if aug.get()=='':
        aug.insert(0,'August')
aug = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
aug.place(x=105,y=220)
aug.insert(0,'August')
aug.bind("<FocusIn>",on_enter)
aug.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    sep.delete(0,'end')
def on_leave(e):
    if sep.get()=='':
        sep.insert(0,'September')
sep = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
sep.place(x=195,y=220)
sep.insert(0,'September')
sep.bind("<FocusIn>",on_enter)
sep.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    octo.delete(0,'end')
def on_leave(e):
    if octo.get()=='':
        octo.insert(0,'October')
octo = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
octo.place(x=25,y=290)
octo.insert(0,'October')
octo.bind("<FocusIn>",on_enter)
octo.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    nov.delete(0,'end')
def on_leave(e):
    if nov.get()=='':
        nov.insert(0,'November')
nov = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
nov.place(x=105,y=290)
nov.insert(0,'November')
nov.bind("<FocusIn>",on_enter)
nov.bind("<FocusOut>",on_leave)

#####---------------------
def on_enter(e):
    dec.delete(0,'end')
def on_leave(e):
    if dec.get()=='':
        dec.insert(0,'December')
dec = Entry(frame,width=10,fg='#ffecd1',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
dec.place(x=195,y=290)
dec.insert(0,'December')
dec.bind("<FocusIn>",on_enter)
dec.bind("<FocusOut>",on_leave)

Button(frame,width=39,pady=7,text='Generate',bg='#EB525D',fg='#ffecd1',border=0,cursor='hand2',
       command=graphing).place(x=25,y=350)




win.mainloop()
