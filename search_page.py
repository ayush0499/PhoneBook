from Tkinter import *
import sqlite3
from tkMessageBox import *

con=sqlite3.Connection('emp')
cur=con.cursor()

def search():

    def f1(q):
        s=''
        g=q.char
        w=str(e.get())
        #print w
        #if ((g>='a' and g<='z' ) or (g>='A' and g<='Z')):
        s=s+w
        #print s
        #s=s+e.get()
        l.delete(0,END)
        cur.execute("select fn,mn,ln from abc where fn like '%{}%' or mn like '%{}%' or ln like '%{}%' or phone like '{}%'".format(w,w,w,w))
        t=cur.fetchall()
        c=0
        for i in t:
            l.insert(c,i)
            c+=1
        #l.delete(0,END)
        def fun(ert):
            def de():
                #v=l.get(l.curselection())
                #v1=v[0]
                cur.execute("delete from abc where fn = (?)and mn=(?)and ln=(?)",(v1,v2,v3))
                con.commit()
                showinfo('info','contact deleted')
                r2.destroy()
            v=l.get(l.curselection())
            v1=v[0]
            v2=v[1]
            v3=v[2]
            l.delete(0,END)
            cur.execute("select * from abc where fn = (?)",(v1,))
            L=cur.fetchall()
            #print L
            counter=0
            l.insert(END,'First Name : '+str(L[0][0]))
            l.insert(END,'Middle Name : '+str(L[0][1]))
            l.insert(END,'Last Name : '+str(L[0][2]))
            l.insert(END,'Company Name : '+str(L[0][3]))
            l.insert(END,'Address : '+str(L[0][4]))
            l.insert(END,'City : '+str(L[0][5]))
            l.insert(END,'Pin Code : '+str(L[0][6]))
            l.insert(END,'website : '+str(L[0][7]))
            l.insert(END,'DOB : '+str(L[0][8]))
            l.insert(END,'Phone type : '+str(L[0][9]))
            l.insert(END,'Phone no : '+str(L[0][10]))
            l.insert(END,'email type : '+str(L[0][11]))
            l.insert(END,'email : '+str(L[0][12]))
            #def ghj(v1):
                #y=askyesno('Delete','do you want to delete')
                #if(y==True):
                    #Button(r2,text="delete",command=de(v1)).grid(row=2,column=3)
                    #cur.execute("delete from abc where fn = (?)",(v1,))
                    #con.commit()
                    #showinfo('info','contact deleted')
            #r2.after(5000,ghj)
            Button(r2,text="delete",font='Times 15 bold',command=de).grid(row=4,column=3)  
            #l.delete(0,END) 
        l.bind('<<ListboxSelect>>',fun)
    r2=Tk()
    r2.title('Search Bar')
    r2.geometry('900x700')
    r2["bg"]="purple"
    Label(r2,text='Searching from PhoneBook',font='Arial20',bg='purple',fg='black').grid(row=0,column=1)
    Label(r2,text='Enter Name or Phone No:',fg="black",font='Arial20',bg='purple').grid(row=2,column=0)
    e=Entry(r2)
    e.grid(row=2,column=1)
    l=Listbox(r2,height=20,width=50,font="Arial5",fg="red",selectmode=SINGLE,bg='black')
    
    
    #z=z+1    
    l.grid(row=3,column=1)
    l.delete(0,END)
    r2.bind('<KeyPress>',f1)
    
    def close():
        r2.destroy()
    Button(r2,text='Close',font='Times 15 bold',command=close).grid(row=4,column=1)
    r2.mainloop()
