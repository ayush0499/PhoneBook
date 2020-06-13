from Tkinter import *
ro=Tk()
#ro['bg']='purple'
#ro.geometry('350x350')
Label(ro,text='Project Title : PhoneBook',font='Arial20',fg='black').grid(row=0,column=0)
Label(ro,text='PYTHON AND DATABASE PROJECT',font='Arial20',fg='blue').grid(row=1,column=2)
Label(ro,text='Developed By : Ayush Dikshit',font='Arial20',fg='red').grid(row=3,column=2)
Label(ro,text='Er : 181b061',font='Arial20',fg='red').grid(row=4,column=2)
Label(ro,text='Batch : B2',font='Arial20',fg='red').grid(row=5,column=2)
Label(ro,text='make a mouse movement to close',font='Arial20',fg='black').grid(row=7,column=2)
def close1(e=1):
    ro.destroy()

ro.bind('<Motion>',close1)
ro.mainloop()
