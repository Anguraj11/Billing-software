from tkinter import *
import mysql.connector
from tkinter.messagebox import showinfo as si
from tkinter.messagebox import showwarning as sw
from tkinter.messagebox import showerror as se
from tkinter import simpledialog as sd


soft=Tk()
im0=PhotoImage(file="signup.png")
im1=PhotoImage(file="images/logo.png")
im2=PhotoImage(file="images/username.png")
im3=PhotoImage(file="images/gmail.png")
im4=PhotoImage(file="images/pwd.png")
im5=PhotoImage(file="images/phone.png")
soft.withdraw()

class page1():
    def __init__(self,sp):
        sp.geometry("1350x750+0+0")
        def create_user():
            n=e1.get()
            e=e2.get()
            p=e3.get()
            ph=e4.get()
            #
            if n=="Name...!" or e=="Email...!" or p=="Password...!" or ph=="Phone...!" or n=="" or e=="" or p=="" or ph=="":
                if n=="Name...!" or n=="":
                    sw("Note : ","You need to enter your name")
                if e=="Email...!" or e=="":
                    sw("Note : ","You need to enter your email")
                if p=="Password...!" or p=="":
                    sw("Note : ","You need to enter your password")
                if ph=="Phone...!" or ph=="":
                    sw("Note : ","You need to enter your number")
            else:
                t=(n,e,p,ph)            
                try:
                    con=mysql.connector.connect(host="localhost",user="root",
                                                password="@angu1221",database="billdp")
                    cur=con.cursor()
                    sql="insert into bill(name,email,pwd,ph) values(%s,%s,%s,%s);"
                    cur.execute(sql,t)
                    con.commit()
                    con.close()
                    si("Success","User Created Successfully...!")
                    login()
                except mysql.connector.errors.IntegrityError as ie:
                    se("Failed","User already exist...!")
                except Exception:
                    se("Sorry","Something went wrong...!")

        def login():
            sp.withdraw()
            from page_2 import page2
            page2(sp)
            sp.deiconify()
#------------design-------------------------------------------------
        ila0=Label(sp,image=im0,bg="white")
        ila0.place(x=0,y=0)

        f1=Frame(sp,width=500,height=750)
        f1.config(bg="white")
        f1.place(x=900,y=0)

        ila1=Label(f1,image=im1,bg="white",bd=10)
        ila1.place(x=200,y=20)

        l0=Label(f1,text="SIGNUP",font=("Constantia","16","bold italic"),bg="white"
                  ,fg="black")
        l0.place(x=200,y=120)

#------------------user--------------------
        il1=Label(f1,image=im2,bg="white")
        il1.place(x=20,y=200)
        def e1event(e):
            e1.delete(0,END)
        def e1leave(e):
            if e1.get()=="":
                e1.insert(0,"Name...!")

        e1=Entry(f1,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=20,bd=0)
        e1.place(x=100,y=215)
        e1.insert(0,"Name...!")
        e1.bind("<FocusIn>",e1event)
        e1.bind("<FocusOut>",e1leave)

#--------------email------------------------
        il2=Label(f1,image=im3,bg="white")
        il2.place(x=20,y=300)
        def e2event(e):
            e2.delete(0,END)
        def e2leave(e):
            if e2.get()=="":
                e2.insert(0,"Email...!")

        e2=Entry(f1,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=20,bd=0)
        e2.place(x=100,y=315)
        e2.insert(0,"Email...!")
        e2.bind("<FocusIn>",e2event)
        e2.bind("<FocusOut>",e2leave)
        
#------------------password-----------------
        il3=Label(f1,image=im4,bg="white")
        il3.place(x=20,y=400)
        def e3event(e):
            e3.delete(0,END)
        def e3leave(e):
            if e3.get()=="":
                e3.insert(0,"Password...!")
        
        e3=Entry(f1,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=20,bd=0)
        e3.place(x=100,y=415)
        e3.insert(0,"Password...!")
        e3.bind("<FocusIn>",e3event)
        e3.bind("<FocusOut>",e3leave)
        

#------------------phone--------------------
        il4=Label(f1,image=im5,bg="white")
        il4.place(x=20,y=500)
        def e4event(e):
            e4.delete(0,END)
        def e4leave(e):
            if e4.get()=="":
                e4.insert(0,"Phone...!")

        e4=Entry(f1,font=("consolas",14,"italic"),bg="#87CEFA",fg="black",width=20,bd=0)
        e4.place(x=100,y=515)
        e4.insert(0,"Phone...!")
        e4.bind("<FocusIn>",e4event)
        e4.bind("<FocusOut>",e4leave)

#-------------------------------------------
        #signup button:--------------------------------------
        b1=Button(f1,text="SIGNUP",font=("Constantia",13,"italic"),bg="#20adcd",fg="#000000",
                  activebackground="black",activeforeground="white",width=10,bd=0,
                  command=create_user)
        b1.place(x=100,y=600)

        b2=Button(f1,text="LOGIN",font=("Constantia",13,"italic"),bg="#20adcd",fg="#000000",
                  activebackground="black",activeforeground="white",width=10,bd=0,
                  command=login)
        b2.place(x=250,y=600)

t=Toplevel(soft)
s=page1(t)
soft.mainloop()
#----------------------------------------------------------------------------------------------
