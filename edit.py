from Tkinter import *
import sqlite3
from tkMessageBox import *

con=sqlite3.Connection('emp')
cur=con.cursor()
def ed():
    r4=Tk()
    r4.title('Edit')
    r4["bg"]='pink'
    Label(r4,text="Enter full name to be edited",font='Arial20',fg='blue',bg='pink').grid(row=0,column=0)
    x=Entry(r4)
    x.grid(row=1,column=0)
    List=Listbox(r4,height=20,width=50,font="Arial5",fg="blue",selectmode=SINGLE,bg='pink')
    List.grid(row=2,column=0)
    

    def ed_search(rt):
        w=str(x.get())
        List.delete(0,END)
        cur.execute("select fn,mn,ln from abc where fn like '%{}%' or mn like '%{}%' or ln like '%{}%'".format(w,w,w))
        t=cur.fetchall()
        c=0
        for i in t:
            List.insert(c,i)
            c+=1

        def ed_edit(yu=4):
            r5=Tk()
            r5.title('Edit details')
            r5["bg"]="pink"
            v1=List.get(List.curselection())
            v11=v1[0]
            v22=v1[1]
            v33=v1[2]
            #print li
            cur.execute('select * from abc where fn=(?) and mn=(?) and ln=(?)',(v11,v22,v33))
            a=cur.fetchall()
            Label(r5,text='First Name',font='Arial20',fg='red',bg='pink').grid(row=4,column=0)
            e1=Entry(r5)
            e1.grid(row=4,column=3)

            Label(r5,text='Middle Name',font='Arial20',fg='red',bg='pink').grid(row=5,column=0)
            e2=Entry(r5)
            e2.grid(row=5,column=3)

            Label(r5,text='Last Name',font='Arial20',fg='red',bg='pink').grid(row=6,column=0)
            e3=Entry(r5)
            e3.grid(row=6,column=3)

            Label(r5,text='Company Name',font='Arial20',fg='red',bg='pink').grid(row=7,column=0)
            e4=Entry(r5)
            e4.grid(row=7,column=3)

            Label(r5,text='Address',font='Arial20',fg='red',bg='pink').grid(row=8,column=0)
            e5=Entry(r5)
            e5.grid(row=8,column=3)

            Label(r5,text='City',font='Arial20',fg='red',bg='pink').grid(row=9,column=0)
            e6=Entry(r5)
            e6.grid(row=9,column=3)

            Label(r5,text='Pin Code',font='Arial20',fg='red',bg='pink').grid(row=10,column=0)
            e7=Entry(r5)
            e7.grid(row=10,column=3)

            Label(r5,text='Website URL',font='Arial20',fg='red',bg='pink').grid(row=11,column=0)
            e8=Entry(r5)
            e8.grid(row=11,column=3)

            Label(r5,text='Date of Birth',font='Arial20',fg='red',bg='pink').grid(row=12,column=0)
            e9=Entry(r5)
            e9.grid(row=12,column=3)

            Label(r5,text='Phone Number',font='Arial20',fg='red',bg='pink').grid(row=14,column=0)
            e10=Entry(r5)
            e10.grid(row=14,column=3)

            Label(r5,text='Email Id',font='Arial20',fg='red',bg='pink').grid(row=16,column=0)
            e11=Entry(r5)
            e11.grid(row=16,column=3)

            e1.insert(0,a[0][0])
            e2.insert(0,a[0][1])
            e3.insert(0,a[0][2])
            e4.insert(0,a[0][3])
            e5.insert(0,a[0][4])
            e6.insert(0,a[0][5])
            e7.insert(0,a[0][6])
            e8.insert(0,a[0][7])
            e9.insert(0,a[0][8])
            e10.insert(0,a[0][10])
            e11.insert(0,a[0][12])

            def finre():
                cur.execute("delete from abc where fn=(?) and mn=(?) and ln=(?)",(v11,v22,v33))
                con.commit()
                try:
                    cur.execute("insert into abc values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),a[0][9],int(e10.get()),a[0][11],e11.get()))
                    con.commit()
                    #cur.execute("select * from abc")
                    #print cur.fetchall()
                    showinfo('info','edited successfully')
                    r5.destroy()
                    r4.destroy()
                except(e):
                    showerror('error',e)

            Button(r5,text="save",font='Times 15 bold',command=finre).grid(row=18,column=2)
            r5.mainloop()
        List.bind('<<ListboxSelect>>',ed_edit)
    
    r4.bind('<KeyPress>',ed_search)   
    #Button(r4,text="next",font='Times 15 bold',command=fined).grid(row=2,column=0)
    r4.mainloop()
