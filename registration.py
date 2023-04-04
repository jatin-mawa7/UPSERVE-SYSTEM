
from tkinter import *
from tkinter import messagebox
#import ast
import pymysql
window=Tk()
window.title("Registration Form")
window.geometry('925x500+300+200')
window.configure(bg='#282633')
window.resizable(False,False)

def clear():
	user.delete(0,END)
	email.delete(0,END)
	addr.delete(0, END)
	phno.delete(0, END)
	aphno.delete(0, END)
	user.insert(0, 'Name')
	email.insert(0, 'Email ID')
	addr.insert(0, 'Address')
	phno.insert(0, 'Phone Number')
	aphno.insert(0, 'Alternate Contact Details')


def register():
	try:
		if user.get()=='Name' or email.get()=='Email ID' or addr.get()=='Address' or phno.get()=='Phone Number' or \
				aphno.get()=='Alternate Contact Details':
			messagebox.showerror('Error','All Fields Are Required')
		else:
			con=pymysql.connect(host='localhost',user='root',password='Root@1234',database='upserve')
			cur=con.cursor()
			cur.execute('select * from customers where email=%s',email.get())
			row=cur.fetchone()
			if row!=None:
				messagebox.showerror('Error','User Already Exists')

			else:
				cur.execute('insert into customers(name,email,address,contact_no,alt_contact_details) values(%s,%s,%s,%s,%s)',
							(user.get(),email.get(),addr.get(),phno.get(),aphno.get()))
				con.commit()
				con.close()

				messagebox.showinfo('Success','Registration Successful')
				clear()


	except Exception as e:
		messagebox.showerror('Error',f'Error due to{e}')


img= PhotoImage(file="img.png")
Label(window,image=img,border=0,bg='#282633').place(x=10,y=90)

frame=Frame(window,width=350,height=390,bg='#282633')
frame.place(x=480,y=50)

heading=Label(frame,text='Registration Form',fg="#57a1f8",bg='#282633',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=20,y=5)


#####---------------------
def on_enter(e):
	user.delete(0,'end')
def on_leave(e):
	if user.get()=='':
		user.insert(0,'Name')


user = Entry(frame,width=25,fg='white',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Name')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='white').place(x=25,y=107)


#####---------------------
def on_enter(e):
	email.delete(0,'end')
def on_leave(e):
	if email.get()=='':
		email.insert(0,'Email ID')


email = Entry(frame,width=25,fg='white',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
email.place(x=30,y=130)
email.insert(0,'Email ID')
email.bind("<FocusIn>",on_enter)
email.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='white').place(x=25,y=157)

#####---------------------
def on_enter(e):
	addr.delete(0,'end')
def on_leave(e):
	if addr.get()=='':
		addr.insert(0,'Address')


addr = Entry(frame,width=25,fg='white',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
addr.place(x=30,y=180)
addr.insert(0,'Address')
addr.bind("<FocusIn>",on_enter)
addr.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='white').place(x=25,y=207)

#####---------------------
def on_enter(e):
	phno.delete(0,'end')
def on_leave(e):
	if phno.get()=='':
		phno.insert(0,'Phone Number')


phno = Entry(frame,width=25,fg='white',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
phno.place(x=30,y=230)
phno.insert(0,'Phone Number')
phno.bind("<FocusIn>",on_enter)
phno.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='white').place(x=25,y=257)

#####---------------------
def on_enter(e):
	aphno.delete(0,'end')
def on_leave(e):
	if aphno.get()=='':
		aphno.insert(0,'Alternate Contact Details')


aphno = Entry(frame,width=25,fg='white',border=0,bg='#282633',font=('Microsoft Yahei UI Light',11))
aphno.place(x=30,y=280)
aphno.insert(0,'Alternate Contact Details')
aphno.bind("<FocusIn>",on_enter)
aphno.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='white').place(x=25,y=307)




#----------------

Button(frame,width=39,pady=7,text='Register',bg='#57a1f8',fg='#282633',border=0,cursor='hand2',command=register).place(x=35,y=350)


'''label=Label(frame,text='I have an account',fg='white',bg='#282633',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign In',border=0, bg='#282633',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=342)'''



window.mainloop()

