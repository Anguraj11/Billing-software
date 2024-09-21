from tkinter import *
import mysql.connector
from tkinter.messagebox import showinfo as si
from tkinter.messagebox import showwarning as sw
from tkinter.messagebox import showerror as se
from tkinter import simpledialog as sd


log=Tk()
lm0=PhotoImage(file="nature.png")
lm1=PhotoImage(file="images/user.png")
lm2=PhotoImage(file="images/username.png")
lm3=PhotoImage(file="images/pwd.png")
log.withdraw()

class page2():
    def __init__(self,par):
        lo=Toplevel(par)
        lo.geometry("1350x750+0+0")
        def signup():
            lo.destroy()
            par.deiconify()
        def check_user():
            e=e1.get()
            p=e2.get()
            t=(e,p)
            con=mysql.connector.connect(host="localhost",user="root",
                                        password="@angu1221",database="billdp")
            cur=con.cursor()
            sql="select * from bill where email = %s and pwd = %s "
            cur.execute(sql,t)
            row=cur.fetchall()
            con.close()
            
            if row==[]:
                se("Failed","No user Found for your email")
                si("Note","Try to Signup and Login")
            else:
                si("Success","Login Success")
                lo.destroy()
                from main_page.load_page import loadcls
                loadcls(par)

#-------------design---------------------------------------------------
        ila0=Label(lo,image=lm0,bg="white")
        ila0.place(x=0,y=0)

        f1=Frame(lo,width=500,height=750)
        f1.config(bg="white")
        f1.place(x=1350,y=0)
        #----------login logo-------
        f2=Frame(lo,width=500,height=350)
        f2.config(bg="white")
        f2.place(x=500,y=200)

        ila1=Label(f2,image=lm1,bg="white")
        ila1.place(x=200,y=10)

        l0=Label(f2,text="LOGIN PAGE",font=("Constantia","10","bold italic"),bg="white"
                  ,fg="black")
        l0.place(x=190,y=70)
#------------------------
        #--------user-------------------------
        il0=Label(f2,image=lm2,bg="white")
        il0.place(x=20,y=120)
        def event(e):
            e1.delete(0,END)
        def leave(e):
            if e1.get()=="":
                e1.insert(0,"Email...!")

        e1=Entry(f2,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=25,bd=0)
        e1.place(x=100,y=135)
        e1.insert(0,"Email...!")
        e1.bind("<FocusIn>",event)
        e1.bind("<FocusOut>",leave)

        il1=Label(f2,image=lm3,bg="white")
        il1.place(x=20,y=200)
        def event1(e):
            e2.delete(0,END)
        def leave1(e):
            if e2.get()=="":
                e2.insert(0,"Password...!")

        e2=Entry(f2,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=25,bd=0)
        e2.place(x=100,y=220)
        e2.insert(0,"Password...!")
        e2.bind("<FocusIn>",event1)
        e2.bind("<FocusOut>",leave1)
#-------------------------------------
        #-----login buttons-------------------
        b1=Button(f2,text="SIGNUP",font=("Constantia",10,"italic"),bg="#20adcd",fg="#000000",
                  activebackground="black",activeforeground="white",width=10,bd=0,
                  command=signup)
        b1.place(x=150,y=280)

        b2=Button(f2,text="LOGIN",font=("Constantia",10,"italic"),bg="#20adcd",fg="#000000",
                  activebackground="black",activeforeground="white",width=10,bd=0,
                  command=check_user)
        b2.place(x=250,y=280)
        log.mainloop()
#--------------------------------------

