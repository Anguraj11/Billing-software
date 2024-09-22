from tkinter import *
from threading import Thread
from time import sleep

class loadcls():
    def __init__(s,par):
        loa=Toplevel(par)
        loa.geometry("1350x750+0+0")
        loa.title("Loading page")
        loa.config(bg="#a4f")
        def load():
            for i in range(-300,1):
                f2.place(x=i,y=0)
                loa.update()
                sleep(0.01)
        def txtload():
            for i in range(1,101):
                l1.config(text=str(i)+"%")
                loa.update()
                sleep(0.040)
            if True:
                loa.withdraw()
                from main_page.app import maincls
                maincls(par)
                
        f1=Frame(loa,width=300,height=25,bg="white")
        f1.place(x=525,y=500)
        
        f2=Frame(f1,width=300,height=25,bg="black")
        f2.place(x=-300,y=0)
        
        l1=Label(f2,text="0%",font=("calibri",12,"bold")
                 ,bg="black",fg="white")
        l1.place(x=265,y=0)

        t1=Thread(target=load)
        t2=Thread(target=txtload)

        t1.start()
        t2.start()

        loa.mainloop()
