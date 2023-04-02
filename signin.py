from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#282634")
root.resizable(False,False)


def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("APP")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Hello Everyone',bg='#fff',font=('Calibri',50,'bold')).pack(expand=True)
        screen.mainloop()

    else:
        messagebox.showerror('Invalid','Invalid username or password')

########****************************************************************************
def signup_command():
    window=Toplevel(root)
      


####################*****************************************
    """elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid","Invalid username or password")

    elif password!='1234':
        messagebox.showerror("Invalid","Invalid Password")
        
    elif username!='admin':
        messagebox.showerror("Invalid","Invalid Username")"""
        #print('UPSERVE')

img = PhotoImage(file='C:\\Users\\DELL\\OneDrive\\Desktop\\mpr\\logo.png')
Label(root,image=img,border=0,width=400,height=400,bg='#78290F').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="#282634")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#ffecd1',bg='#282634',font=('Georgia',23,'bold'))
heading.place(x=120,y=5)

####################---------------------------------------

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
    
user=Entry(frame,width=25,fg='#ffecd1',border=0,bg='#282634',font=('Georgia',11))
user.place(x=80,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='#ffecd1').place(x=75,y=107)

####################---------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='#ffecd1',border=0,bg='#282634',font=('Georgia',11))
code.place(x=80,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='#ffecd1').place(x=75,y=177)


############------------------------------

Button(frame,width=30,pady=7,text='Sign In',font=('Georgia'),bg='#f44459',fg='#ffecd1',border=0,command=signin).place(x=75,y=204)
label=Label(frame,text="Don't have an account?",fg='#918c9c',bg='#282634',font=('Georgia',9))
label.place(x=75,y=250)

sign_up=Button(frame,width=6,text='Sign Up',border=0,font=('Georgia',9),bg='#282634',cursor='hand2',fg='#ffecd1',command=signup_command)
sign_up.place(x=230,y=250)

root.mainloop()
