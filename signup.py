from tkinter import *
from tkinter import messagebox
import ast



window = Tk()
window.title("Sign up")
window.geometry('925x500+300+200')
window.configure(bg="#282634")
window.resizable(False, False)


def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('SIGNUP', 'Successfully signed up!')

        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid", "Passowords do not match")


def sign():

    window.destroy()


img = PhotoImage(file='img.png')
Label(window, image=img, border=0, width=400, height=400, bg='#78290F').place(x=50, y=50)

frame = Frame(window, width=400, height=400, bg='#282634')
frame.place(x=480, y=50)

heading = Label(frame, text='SIGN UP', fg='#ffecd1', bg='#282634', font=('Georgia', 23, 'bold'))
heading.place(x=120, y=5)


#######---------------------------------
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='#ffecd1', border=0, bg='#282634', font=('Georgia', 11))
user.place(x=80, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='#ffecd1').place(x=75, y=107)


###############-----------------------
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='#ffecd1', border=0, bg='#282634', font=('Georgia', 11))
code.place(x=80, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='#ffecd1').place(x=75, y=177)


###############-----------------------
def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    name = confirm_code.get()
    if name == '':
        confirm_code.insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, fg='#ffecd1', border=0, bg='#282634', font=('Georgia', 11))
confirm_code.place(x=80, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='#ffecd1').place(x=75, y=247)
###############-----------------------
Button(frame, width=32, pady=7, text='SIGN UP', font=('Georgia'), bg='#f44459', fg='#ffecd1', border=0,
       command=signup).place(x=75, y=280)
label = Label(frame, text='I have an account', fg='#918c9c', bg='#282634', font=('Georgia', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign In', border=0, bg='#282634', cursor='hand2', fg='#ffecd1', command=sign)
signin.place(x=200, y=340)


window.mainloop()
