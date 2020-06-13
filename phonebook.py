from Tkinter import *
from datetime import date
from cover import *
import sqlite3
from edit import *
#from save_page import *
from search_page import *
from tkMessageBox import *

con=sqlite3.Connection('emp')
cur=con.cursor()
cur.execute("create table if not exists abc(fn varchar(20),mn varchar(20),ln varchar(20),cn varchar(20) ,address varchar(50),city varchar(10),pin number(6),wbs varchar(20),dob date,ph_type varchar(10),phone number(10),em_type varchar(10),email varchar(20))")
root=Tk()
root.title('PhoneBook')
root.geometry('750x750')
root["bg"]="dark green"

im=PhotoImage(file='images1.gif')
Label(root,image=im).grid(row=0,column=2)

Label(root,text='First Name',font='Times 17 bold',fg='black',bg='dark green').grid(row=4,column=0)
e1=Entry(root)
e1.grid(row=4,column=3)

Label(root,text='Middle Name',font='Times 17 bold',fg='black',bg='dark green').grid(row=5,column=0)
e2=Entry(root)
e2.grid(row=5,column=3)

Label(root,text='Last Name',font='Times 17 bold',fg='black',bg='dark green').grid(row=6,column=0)
e3=Entry(root)
e3.grid(row=6,column=3)

Label(root,text='Company Name',font='Times 17 bold',fg='black',bg='dark green').grid(row=7,column=0)
e4=Entry(root)
e4.grid(row=7,column=3)

Label(root,text='Address',font='Times 17 bold',fg='black',bg='dark green').grid(row=8,column=0)
e5=Entry(root)
e5.grid(row=8,column=3)

Label(root,text='City',font='Times 17 bold',fg='black',bg='dark green').grid(row=9,column=0)
e6=Entry(root)
e6.grid(row=9,column=3)

Label(root,text='Pin Code',font='Times 17 bold',fg='black',bg='dark green').grid(row=10,column=0)
e7=Entry(root)
e7.grid(row=10,column=3)

Label(root,text='Website URL',font='Times 17 bold',fg='black',bg='dark green').grid(row=11,column=0)
e8=Entry(root)
e8.grid(row=11,column=3)

Label(root,text='Date of Birth',font='Times 17 bold',fg='black',bg='dark green').grid(row=12,column=0)
e9=Entry(root)
e9.grid(row=12,column=3)

Label(root,text='Select PhoneType',font='Times 17 bold',fg='purple',bg='dark green').grid(row=13,column=0)
v1=IntVar()
Radiobutton(root,text='Office',font='Times 15 bold',variable=v1,value=1,bg='dark green').grid(row=13,column=2)
Radiobutton(root,text='Home',font='Times 15 bold',variable=v1,value=2,bg='dark green').grid(row=13,column=3)
Radiobutton(root,text='Mobile',font='Times 15 bold',variable=v1,value=3,bg='dark green').grid(row=13,column=15)

Label(root,text='Phone Number',font='Times 17 bold',fg='black',bg='dark green').grid(row=14,column=0)
e10=Entry(root)
e10.grid(row=14,column=3)

Button(root,text='+').grid(row=14,column=15)

Label(root,text='Select Email Type',font='Times 17 bold',fg='purple',bg='dark green').grid(row=15,column=0)
v2=IntVar()
Radiobutton(root,text='Office',font='Times 15 bold',variable=v2,value=1,bg='dark green').grid(row=15,column=2)
Radiobutton(root,text='Personal',font='Times 15 bold',variable=v2,value=2,bg='dark green').grid(row=15,column=3)

Label(root,text='Email Id',font='Times 17 bold',fg='black',bg='dark green').grid(row=16,column=0)
e11=Entry(root)
e11.grid(row=16,column=3)

Button(root,text='+').grid(row=16,column=15)



def save():
    er=er1=er2=er3=er4=0
    
    a=e1.get()
    b=e2.get()
    c=e3.get()
    try:
        assert (not(a==b and c==b)),"first,middle and last name neither can be same nor can be null."
    except AssertionError as error:
        er=1
        showerror('error',error)
    d=e4.get()
    e=e5.get()
    f=e6.get()

    try:
        assert(not((e7.get()).isdigit()==False or len(e7.get())!=6)),"pin should be num of 6 digits"
    except AssertionError as error:
        er1=1
        showerror('error',error)
    if er1==0:
        g=int(e7.get())
    
    h=e8.get()
    k=e9.get()
    if len(k)==0:
        showerror('error',"Please enter DoB")
    else:
        da= date.today()
        doby=k[6:]
        ye=da.year
        mo=k[3:5]
        dy=k[0:2]
        try:
            assert (not((int(dy)<1) or (int(dy)>31) or (int(mo)<1) or (int(mo)>12) or (int(ye)-int(doby))<16)),"You are either underage or date format is wrong"
        
        except AssertionError as error:    
            er2=1
            showerror('error',error)
    
    i=int(v1.get())
    if i==1:
        j='Office'
    elif i==2:
        j='Home'
    elif i==3:
        j='Mobile'

    try:
        assert(not((e10.get()).isdigit()==False or len(e10.get())!=10)),"phone should be a num of 10 digits"
    except AssertionError as error:
        #if ta==1 or len(ent10.get())!=10:
        er3=1
        showerror('error',error)
    if er3==0:
        p=int(e10.get())
    l=int(v2.get())
    if l==1:
        m='Office'
    elif l==2:
        m='Personal'
    n=e11.get()
    try:
        assert (not(n.count('@')!=1 or n.count('.')!=1)),"email contains only one @ and (.) characters"
    except AssertionError as error:
        er4=1
        showerror('error',error)

    if er==0 and er1==0 and er2==0 and er3==0 and er4==0:
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        cur.execute("insert into abc values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,k,j,p,m,n))
        con.commit()
        showinfo('info','Saved successfully')




        
def Close():
    #cur.execute("select * from abc")
    #print(cur.fetchall())
    root.destroy()


Button(root,text='Save',font='Times 15 bold',command=save).grid(row=25,column=0)
Button(root,text='Search',font='Times 15 bold',command=search).grid(row=25,column=2)
Button(root,text='Close',font='Times 15 bold',command=Close).grid(row=25,column=3)
Button(root,text='Edit',font='Times 15 bold',command=ed).grid(row=25,column=15)

root.mainloop()
