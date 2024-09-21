from tkinter import *
from tkinter import ttk
import customtkinter
import mysql.connector
from tkinter.messagebox import showinfo as si
from tkinter.messagebox import showwarning as sw
from tkinter.messagebox import showerror as se
from tkinter import simpledialog as sd
from time import sleep
import csv
from email.message import EmailMessage
import ssl
import smtplib


DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")
        

class maincls():
    def __init__(self,par):
        def cust():
            def clear():
                c1.delete(0,END)
                c2.delete(0,END)
                c3.delete(0,END)
                c4.delete(0,END)

            def cread():
                #pre-processing
                clear()
                r=sd.askstring("Note","Please enter the ID number to View :")
                #print("r is",r)
                
                #connection
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                            database="stockdp")
                #print("Read Suucess")
                cur=con.cursor()
                sql=f"select * from customer where cid = {r}"
                cur.execute(sql)# it will execute the Query in MySQL
                row=cur.fetchall()# it is used to get the output From MySQL
                #print("row is",row)
                con.close()
                if row==[]:
                    sw("warning",f"No ID found for {r}")
                    si("Note","Try give valid ID to read")
                else:
                    def fun(a):
                        #print("a is",a)
                        fun2(*a)
                    def fun2(i,n,p,e):
                        #print(a,b,c,d)
                        c4.insert(0,i)
                        c1.insert(0,n)
                        c2.insert(0,p)
                        c3.insert(0,e)
                    fun(*row)

            def cusup():
                try:
                    # Get values from entry fields
                    i=c4.get()
                    n=c1.get()
                    ph=c2.get()
                    e=c3.get()
                    
                    # Check if required fields are not empty
                    if i and n and ph and e:
                        # Connect to the database
                        con = mysql.connector.connect(host="localhost", user="root", password="@angu1221", database="stockdp")
                        cur = con.cursor()
                        
                        # Prepare data tuple for SQL query
                        t = (n,ph,e,i)
                        
                        # SQL update query
                        sql = "UPDATE customer SET cname=%s, cphone=%s, cemail=%s WHERE cid=%s;"
                        
                        # Execute the query
                        cur.execute(sql, t)
                        
                        # Commit changes and close connection
                        con.commit()
                        con.close()
                        
                        # Show success message
                        si("Success", "Updated Successfully")
                        
                        # Clear entry fields
                        clear()
                    else:
                        # Show a warning if any required field is empty
                        sw("Note", "Please fill in all fields")
                except mysql.connector.Error as e:
                    # Handle MySQL errors
                    print("MySQL Error:", e)
                    sw("Error", "Failed to update record. Please try again.")

            
            def cuspre():
                
                cn=c1.get()
                cp=c2.get()
                ce=c3.get()
                if cn=="" or ce=="" or cp=="":
                    if cn=="":
                        sw("Note : ","You need to enter your name")
                        if ce=="":
                            sw("Note : ","You need to enter your email")
                            if cp=="":
                                sw("Note : ","You need to enter your Number")
                    else :
                        t=(cn,cp,ce)            

                        try:
                            con=mysql.connector.connect(host="localhost",user="root",
                                                            password="@angu1221",database="stockdp")
                            cur=con.cursor()
                            sql="insert into customer(cname,cphone,cemail) values(%s,%s,%s);"
                            cur.execute(sql,t)
                            con.commit()
                            con.close()
                            si("Success","Added Successfully...!")
                        except mysql.connector.errors.IntegrityError as ie:
                            se("Failed"," Already exist...!")
                        except Exception:
                            se("Sorry","Something went wrong...!")
             
            cab1=customtkinter.CTkFrame(ang,width=1050,height=700,fg_color="white")
            cab1.place(x=310,y=20)

            clab1=customtkinter.CTkLabel(cab1,text="Customer Name ",text_color="black",
                                         font=("Constantia",20))
            clab1.place(x=50,y=150)

            c1=customtkinter.CTkEntry(cab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            c1.place(x=200,y=150)

            clab2=customtkinter.CTkLabel(cab1,text="Phone NO ",text_color="black",
                                         font=("Constantia",20))
            clab2.place(x=50,y=200)

            c2=customtkinter.CTkEntry(cab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            c2.place(x=200,y=200)
 
            clab3=customtkinter.CTkLabel(cab1,text="Email ",text_color="black",
                                         font=("Constantia",20))
            clab3.place(x=50,y=250)

            c3=customtkinter.CTkEntry(cab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            c3.place(x=200,y=250)

            clab4=customtkinter.CTkLabel(cab1,text="C-ID ",text_color="black",
                                         font=("Constantia",20))
            clab4.place(x=50,y=300)

            c4=customtkinter.CTkEntry(cab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            c4.place(x=200,y=300)

            bt=Button(cab1,text="Exist",fg="black",
                      width=10,bg="red",command=cab1.destroy)
            bt.place(x=10,y=20)

            cabt1=customtkinter.CTkButton(cab1,text="ADD",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=cuspre)
            cabt1.place(x=450,y=150)

            cabt2=customtkinter.CTkButton(cab1,text="Update",text_color="black",
                                          width=85,fg_color="#FFEE4D",command=cusup)
            cabt2.place(x=450,y=200)

            cabt3=customtkinter.CTkButton(cab1,text="Read",text_color="black",
                                          width=85,fg_color="#FFEE4D",command=cread)
            cabt3.place(x=450,y=250)
        
        def table():
            root = Tk()
            root.title("STOCK INFORMATION")
            root.resizable(False, False)

            connection = mysql.connector.connect(host='localhost', user='root', port='3306',
                                                 password='@angu1221', database='stockdp')
            c = connection.cursor()

            frame = Frame(root, bg="black")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            trv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), height=15, show="headings")
            trv.grid(row=0, column=0, sticky="nsew")

            scrollbar = Scrollbar(frame, orient="vertical", command=trv.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")
            trv.configure(yscrollcommand=scrollbar.set)

            trv.column(1, anchor=CENTER, width=100)
            trv.column(2, anchor=CENTER, width=100)
            trv.column(3, anchor=CENTER, width=100)
            trv.column(4, anchor=CENTER, width=100)
            trv.column(5, anchor=CENTER, width=100)
            trv.column(6, anchor=CENTER, width=100)

            trv.heading(1, text="Stock ID")
            trv.heading(2, text="Product Name")
            trv.heading(3, text="Quantity")
            trv.heading(4, text="Rate")
            trv.heading(5, text="Manufacture")
            trv.heading(6, text="Category")

            # Use the cursor object to execute a SELECT statement
            c.execute("select * from stock_tab")

            # Fetch all the rows of data
            rows = c.fetchall()

            # Insert the data into the Treeview
            for row in rows:
                trv.insert('', 'end', values=row)

            frame.pack()
            root.mainloop()



        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)

        def product():
            
            def creation():
                p=e1.get()
                q=e2.get()
                r=e3.get()
                m=e4.get()
                c=e5.get()
                t=(p,q,r,m,c)            
                try:
                    con=mysql.connector.connect(host="localhost",user="root",
                                                password="@angu1221",database="stockdp")
                    cur=con.cursor()
                    sql="insert into stock_tab (pname, qty, rate, manu, cata) values(%s,%s,%s,%s,%s);"
                    cur.execute(sql,t)
                    con.commit()
                    con.close()
                    si("Success","Added Successfully...!")
                except mysql.connector.errors.IntegrityError as ie:
                    se("Failed"," Already exist...!")
                except Exception:
                    se("Sorry","Something went wrong...!")
                
            tab1=customtkinter.CTkFrame(ang,width=1050,height=700,fg_color="white")
            tab1.place(x=310,y=20)

            flab1=customtkinter.CTkLabel(tab1,text="Product Name ",text_color="black",
                                         font=("Constantia",20))
            flab1.place(x=50,y=150)

            e1=customtkinter.CTkEntry(tab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            e1.place(x=200,y=150)

            flab2=customtkinter.CTkLabel(tab1,text="Quantity ",text_color="black",
                                         font=("Constantia",20))
            flab2.place(x=50,y=200)

            e2=customtkinter.CTkEntry(tab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            e2.place(x=200,y=200)
 
            flab3=customtkinter.CTkLabel(tab1,text="Rate ",text_color="black",
                                         font=("Constantia",20))
            flab3.place(x=50,y=250)

            e3=customtkinter.CTkEntry(tab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            e3.place(x=200,y=250)

            flab4=customtkinter.CTkLabel(tab1,text="Manufacture ",text_color="black",
                                         font=("Constantia",20))
            flab4.place(x=50,y=300)

            e4=customtkinter.CTkEntry(tab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            e4.place(x=200,y=300)

            flab5=customtkinter.CTkLabel(tab1,text="Category ",text_color="black",
                                         font=("Constantia",20))
            flab5.place(x=50,y=350)

            e5=customtkinter.CTkEntry(tab1,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            e5.place(x=200,y=350)

            tabt1=customtkinter.CTkButton(tab1,text="Add",text_color="black",
                                        width=100,fg_color="#FFEE4D",command=creation)
            tabt1.place(x=350,y=400)
            
            bt1=customtkinter.CTkButton(tab1,text="Exist",text_color="black",
                                        width=10,fg_color="red",command=tab1.destroy)
            bt1.place(x=10,y=20)
            

        def update():
            
            def clearall():
                en1.delete(0,END)
                en2.delete(0,END)
                en3.delete(0,END)
                en4.delete(0,END)
                en5.delete(0,END)
                en6.delete(0,END)

            def read():
                global r
                #pre-processing
                clearall()
                r=sd.askstring("Note","Please enter the ID number to View :")
                #print("r is",r)
                
                #connection
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                            database="stockdp")
                #print("Read Suucess")
                cur=con.cursor()
                sql=f"select * from stock_tab where sid = {r}"
                cur.execute(sql)# it will execute the Query in MySQL
                row=cur.fetchall()# it is used to get the output From MySQL
                #print("row is",row)
                con.close()
                if row==[]:
                    sw("warning",f"No ID found for {r}")
                    si("Note","Try give valid ID to read")
                else:
                    def fun(a):
                        #print("a is",a)
                        fun2(*a)
                    def fun2(a,b,c,d,e,f):
                        #print(a,b,c,d)
                        en1.insert(0,a)
                        en2.insert(0,b)
                        en3.insert(0,c)
                        en4.insert(0,d)
                        en5.insert(0,e)
                        en6.insert(0,f)
                    fun(*row)

            def updation():
                try:
                    # Get values from entry fields
                    i = en1.get()
                    n = en2.get()
                    q = en3.get()
                    a = en4.get()
                    m = en5.get()
                    c = en6.get()
                    
                    # Check if required fields are not empty
                    if i and n and q and a and m and c:
                        # Connect to the database
                        con = mysql.connector.connect(host="localhost", user="root", password="@angu1221", database="stockdp")
                        cur = con.cursor()
                        
                        # Prepare data tuple for SQL query
                        t = (n, q, a, m, c, i)
                        
                        # SQL update query
                        sql = "UPDATE stock_tab SET pname=%s, qty=%s, rate=%s, manu=%s, cata=%s WHERE sid=%s;"
                        
                        # Execute the query
                        cur.execute(sql, t)
                        
                        # Commit changes and close connection
                        con.commit()
                        con.close()
                        
                        # Show success message
                        si("Success", "Updated Successfully")
                        
                        # Clear entry fields
                        clearall()
                    else:
                        # Show a warning if any required field is empty
                        sw("Note", "Please fill in all fields")
                except mysql.connector.Error as e:
                    # Handle MySQL errors
                    print("MySQL Error:", e)
                    sw("Error", "Failed to update record. Please try again.")
            
            tab2=customtkinter.CTkFrame(ang,width=1050,height=700,fg_color="#82CDCD")
            tab2.place(x=310,y=20)
            bt2=customtkinter.CTkButton(tab2,text="Exist",text_color="black",
                                        width=10,fg_color="red",command=tab2.destroy)
            bt2.place(x=10,y=20)

            fab1=customtkinter.CTkLabel(tab2,text="Stock ID ",text_color="black",
                                         font=("Constantia",20))
            fab1.place(x=50,y=150)

            en1=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en1.place(x=200,y=150)

            fab2=customtkinter.CTkLabel(tab2,text="Product Name ",text_color="black",
                                         font=("Constantia",20))

            fab2.place(x=50,y=200)

            en2=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en2.place(x=200,y=200)
 
            fab3=customtkinter.CTkLabel(tab2,text="Quantity ",text_color="black",
                                         font=("Constantia",20))
            fab3.place(x=50,y=250)

            en3=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en3.place(x=200,y=250)

            fab4=customtkinter.CTkLabel(tab2,text="Rate  ",text_color="black",
                                         font=("Constantia",20))
            fab4.place(x=50,y=300)

            en4=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en4.place(x=200,y=300)

            fab5=customtkinter.CTkLabel(tab2,text="Manufacture ",text_color="black",
                                         font=("Constantia",20))
            fab5.place(x=50,y=350)

            en5=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en5.place(x=200,y=350)

            fab6=customtkinter.CTkLabel(tab2,text="Category ",text_color="black",
                                         font=("Constantia",20))
            fab6.place(x=50,y=400)

            en6=customtkinter.CTkEntry(tab2,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en6.place(x=200,y=400)


            tabt2=customtkinter.CTkButton(tab2,text="Update",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=updation)
            tabt2.place(x=350,y=450)
            
            tabt3=customtkinter.CTkButton(tab2,text="Read",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=read)
            tabt3.place(x=450,y=450)

                
        def delete():
            def deletion():
                r=sd.askstring("Note","Please enter the ID number to Delete :")
                
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                            database="stockdp")

                cur=con.cursor()
                #print("deleteing....")
                sql="delete from stock_tab where sid = "+r
                cur.execute(sql)
                con.commit()#it is used to save the progress
                con.close()

            tab3=customtkinter.CTkFrame(ang,width=1050,height=700,fg_color="#CDEBEB")
            tab3.place(x=310,y=20)
            bt3=customtkinter.CTkButton(tab3,text="Exist",text_color="black",
                                        width=10,fg_color="red",command=tab3.destroy)
            bt3.place(x=10,y=20)

            
            fab1=customtkinter.CTkLabel(tab3,text="Stock ID ",text_color="black",
                                         font=("Constantia",20))
            fab1.place(x=50,y=150)

            en1=customtkinter.CTkEntry(tab3,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en1.place(x=200,y=150)

            fab2=customtkinter.CTkLabel(tab3,text="Product Name ",text_color="black",
                                         font=("Constantia",20))
            fab2.place(x=50,y=200)

            en2=customtkinter.CTkEntry(tab3,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en2.place(x=200,y=200)
 
            fab3=customtkinter.CTkLabel(tab3,text="Quantity ",text_color="black",
                                         font=("Constantia",20))
            fab3.place(x=50,y=250)

            en3=customtkinter.CTkEntry(tab3,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en3.place(x=200,y=250)

            fab4=customtkinter.CTkLabel(tab3,text="Rate  ",text_color="black",
                                         font=("Constantia",20))
            fab4.place(x=50,y=300)

            en4=customtkinter.CTkEntry(tab3,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en4.place(x=200,y=300)

            fab5=customtkinter.CTkLabel(tab3,text="Manufacture ",text_color="black",
                                         font=("Constantia",20))
            fab5.place(x=50,y=350)

            en5=customtkinter.CTkEntry(tab3,font=("consolas",14,"italic"),
                                      fg_color="black",width=200)
            en5.place(x=200,y=350)

            tabt4=customtkinter.CTkButton(tab3,text="Delete",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=deletion)
            tabt4.place(x=350,y=400)
            
            tabt5=customtkinter.CTkButton(tab3,text="Read",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=table)
            tabt5.place(x=450,y=400)
        def create_bill():                
            #------------bill_view-----------------------------------------------------------
            def billview():
                btab=Frame(ang,width=1050,height=700,bg="#CDEBEB")
                btab.place(x=310,y=20)

                bt=Button(btab,text="Exist",fg="black",
                      width=10,bg="red",command=btab.destroy)
                bt.place(x=10,y=20)
#               __________
                def clr_prd():
                    con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                        database="temp_cus")
                    cur=con.cursor()
                    sql="truncate table temp_stock ;"
                    cur.execute(sql)
                    con.commit()
                    con.close()
                    tree3()
                def billwriter():
                    l1=[]
                    l1.append(ce1.get())
                    l1.append(ce2.get())
                    l1.append(ce4.get())

                    if ce1.get()=="" or ce1.get()=="" or ce1.get()=="":
                        si("Note ","You need to select the customer First ... ! ")
                        
                    else:
                        
                        con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                            database="temp_cus")
                        cur=con.cursor()
                        sql="select * from temp_stock ;"
                        cur.execute(sql)
                        row=cur.fetchall()
                        con.close()
                        
                        self.body1=row
                        self.email=l1[-1]
                        
                        prds=[]
                        prds.append(["",])
                        prds.append(l1)
                        for i in row:
                            temp=[]
                            for j in i:
                                temp.append(j)
                            prds.append(temp)
                        print(l1)
                        print(prds)
                        self.last=prds
                        # Data to append
                        new_data = prds
                        # Path to the existing CSV file
                        file_path = "bill.csv"
                        # Open the existing file in append mode
                        with open(file_path, mode='a', newline='') as file:
                            writer = csv.writer(file)
                            # Append each row of new data to the CSV file
                            for i in new_data:
                                writer.writerow(i)
                        print("Data appended successfully.")

                    pass
                
                def tree3():    
                    myTree2=ttk.Treeview(btab,height=15)
                    myTree2['columns']=("","Pid","Product Name","Purchased Quantity","Rate","Total Rate")
                    myTree2.column('#0',width=0,stretch=NO)
                    #1st column always as empty
                    #stretch=NO means it will remove the 0th column 
                    myTree2.column("#1",width=130,anchor=CENTER)
                    myTree2.column("#2",width=130,anchor=CENTER)
                    myTree2.column("#3",width=130,anchor=CENTER)
                    myTree2.column("#4",width=130,anchor=CENTER)
                    myTree2.column("#5",width=130,anchor=CENTER)
                    #in above code we are defining the column 1st then mention the headings below
                    myTree2.heading("#0",text="")# 1st column always empty
                    myTree2.heading("#1",text="Pid")
                    myTree2.heading("#2",text="Product Name")
                    myTree2.heading("#3",text="Purchased Quantity")
                    myTree2.heading("#4",text="Rate")
                    myTree2.heading("#5",text="Total Rate")
                    con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                    database="temp_cus")
                    cur=con.cursor()
                    sql="select pid,proname,qty,rate,totalrate from temp_stock"
                    cur.execute(sql)
                    row=cur.fetchall()
                    
                    con.close()
                    #Dummy Records
                    #myTree1.insert("",index=0,values=(1,"Krish","Tirupur","9994974215","krishleesya@gmail.com"))
                    #add multiple records using for loop
                    self.sno1=0
                    
                    for i in row:
                        if self.sno1%2==0:
                            myTree2.insert("",index="end",iid=self.sno1,values=(i[0],i[1],i[2],i[3],i[4]),tags=("even",))
                        else:
                            myTree2.insert("",index="end",iid=self.sno1,values=(i[0],i[1],i[2],i[3],i[4]),tags=("low",))
                        self.sno1+=1
                    
                    myTree2.tag_configure("low",font=("calibri",12,"bold"),background="red",foreground="white")
                    myTree2.tag_configure("high",font=("calibri",12,"bold"),background="green",foreground="white")
                    myTree2.tag_configure("even",font=("calibri",12,"bold"),background="white",foreground="black")

                    myTree2.place(x=10,y=100)

                tree3()
                def send_em():
                    print(self.last)
                    try:
                        email_sender = 'anguraj.s0420@gmail.com'    
                        password = "ppyn mydl udej cgep"
                        
                        email_receiver =f'{self.email}'
                        subject="Product Purchased Detail's : "

                        body=""
                        tot_amt=0
                        for i in self.body1:
                            tot_amt=tot_amt+int(i[-1])
                            for j in i:
                                body=body+str(j)+"  "
                            body=body+"\n"
                        body=body+"Total Amount : "+str(tot_amt)+"  \n"
                        em=EmailMessage()
                        em["From"]=email_sender
                        em["To"]=email_receiver
                        em["Subject"]=subject
                        em.set_content(body)
                        context=ssl.create_default_context()

                        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                            smtp.login(email_sender,password)
                            smtp.sendmail(email_sender,email_receiver,em.as_string())
                        si("Success","Email sent Successfully...!")
                    except Exception as e:
                        sw("ERROR","Cannot send the email...!")
                mybt1=customtkinter.CTkButton(btab,text="Proceed",text_color="black",
                                        width=90,fg_color="#FFEE4D",command=billwriter)
                mybt1.place(x=300,y=450)

                mybt2=customtkinter.CTkButton(btab,text="Clearall",text_color="black",
                                        width=90,fg_color="#FFEE4D",command=clr_prd)
                mybt2.place(x=400,y=450)
                
                vbbt3=customtkinter.CTkButton(btab,text="Generate",text_color="black",
                                                width=85,fg_color="#FFEE4D",command=send_em)
                vbbt3.place(x=300,y=500)
#               ________
                
            tab=Frame(ang,width=1050,height=700,bg="#CDEBEB")
            tab.place(x=310,y=20)

            sla1=customtkinter.CTkLabel(tab,text="Stock ID",text_color="black",font=("Constantia",20))
            sla1.place(x=10,y=100)

            se1=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            se1.place(x=150,y=100)

            sla2=customtkinter.CTkLabel(tab,text="Product Name",text_color="black",font=("Constantia",20))
            sla2.place(x=10,y=150)

            se2=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            se2.place(x=150,y=150)

            sla3=customtkinter.CTkLabel(tab,text="Quantity",text_color="black",font=("Constantia",20))
            sla3.place(x=10,y=200)

            se3=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            se3.place(x=150,y=200)

            sla4=customtkinter.CTkLabel(tab,text="Rate",text_color="black",font=("Constantia",20))
            sla4.place(x=10,y=250)

            se4=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            se4.place(x=150,y=250)

            cla1=customtkinter.CTkLabel(tab,text="CusID",text_color="black",font=("Constantia",20))
            cla1.place(x=10,y=350)

            ce1=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            ce1.place(x=150,y=350)

            cla2=customtkinter.CTkLabel(tab,text="Cust Name",text_color="black",font=("Constantia",20))
            cla2.place(x=10,y=400)

            ce2=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            ce2.place(x=150,y=400)

            cla3=customtkinter.CTkLabel(tab,text="Phone No",text_color="black",font=("Constantia",20))
            cla3.place(x=10,y=450)

            ce3=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            ce3.place(x=150,y=450)

            cla4=customtkinter.CTkLabel(tab,text="Email",text_color="black",font=("Constantia",20))
            cla4.place(x=10,y=500)

            ce4=customtkinter.CTkEntry(tab,font=("consolas",14,"italic"),
                                      fg_color="black",width=150)
            ce4.place(x=150,y=500)


            bt=Button(tab,text="Exist",fg="black",
                      width=10,bg="red",command=tab.destroy)
            bt.place(x=10,y=20)
            def tree1():
                ##################
                #-----Treeview---------> 1
                ##################
                #create Treeview
                myTree=ttk.Treeview(tab,height=15)
                myTree['columns']=("","Stock ID","Product Name","Quantity","Rate")
                myTree.column('#0',width=0,stretch=NO)
                #1st column always as empty
                #stretch=NO means it will remove the 0th column 
                myTree.column("#1",width=130)
                myTree.column("#2",width=130)
                myTree.column("#3",width=130)
                myTree.column("#4",width=130)
                #in above code we are defining the column 1st then mention the headings below
                myTree.heading("#0",text="")# 1st column always empty
                myTree.heading("#1",text="Stock ID")
                myTree.heading("#2",text="Product Name")
                myTree.heading("#3",text="Quantity")
                myTree.heading("#4",text="Rate")

                #Dummy Records
                #myTree.insert("",index=0,values=(1,"Krish","Tirupur","9994974215","krishleesya@gmail.com"))
                #add multiple records using for loop
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                database="stockdp")
                cur=con.cursor()
                sql="select sid,pname,qty,rate from stock_tab"
                cur.execute(sql)
                row=cur.fetchall()
                
                con.close()
                self.sno=1
                
                for i in row:
                    if int(i[2])<=15:
                        myTree.insert("",index="end",iid=self.sno,values=(i[0],i[1],i[2],i[3]),tags=("low",))
                    elif int(i[2]>=70):
                        myTree.insert("",index="end",iid=self.sno,values=(i[0],i[1],i[2],i[3]),tags=("high",))
                    else:
                        myTree.insert("",index="end",iid=self.sno,values=(i[0],i[1],i[2],i[3]),tags=("even",))
                    self.sno+=1
                    
                myTree.tag_configure("low",font=("calibri",12,"bold"),background="red",foreground="white")
                myTree.tag_configure("high",font=("calibri",12,"bold"),background="green",foreground="white")
                myTree.tag_configure("even",font=("calibri",12,"bold"),background="white",foreground="black")
                myTree.place(x=525,y=5)
                def mybind1(e):
                    sel=myTree.focus()
                    print(sel)
                    vls=myTree.item(sel,"values")
                    print(vls)
                    print(dir(sd))
                    sdv=sd.askstring("Note :",f"Enter the Quantity total Qty :{vls[2]}:")
                    print("sdv is",sdv)
                    se1.delete(0,END)
                    se2.delete(0,END)
                    se3.delete(0,END)
                    se4.delete(0,END)
                    
                    se1.insert(0,vls[0])
                    se2.insert(0,vls[1])
                    try:
                        se3.insert(0,sdv)
                        se4.insert(0,vls[3])
                    except Exception as e:
                        se1.delete(0,END)
                        se2.delete(0,END)
                myTree.bind("<ButtonRelease-1>",mybind1)
            
            ##################
            #-----Treeview---------> 2
            ##################
            def checkout():
                print("\n\t\t\tchecking out products\n")
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                database="stockdp")
                tup=(se1.get(),)
                cur=con.cursor()
                sql="select qty from stock_tab where sid= %s "
                cur.execute(sql,tup)
                row=cur.fetchall()
                #print("stocks on hand",row)
                con.close()

                qty_r=int(se3.get())
                t_qty=row[0]
                t_qty=int(t_qty[0])
                #print("total qty",t_qty)
                #print("qty reqired",qty_r)
                if qty_r>t_qty:
                    sw("Warning","NOT ENOUGH SUPPLIES...!")
                    si("Note",f"We have only {t_qty} left you are asking for {qty_r}")
                else:
                    si("Ok","Products added")
                    t_qty=t_qty - qty_r
                    con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                    database="stockdp")
                    tup=(t_qty,se1.get())
                    cur=con.cursor()
                    sql="update stock_tab set qty= %s where sid= %s "
                    cur.execute(sql,tup)
                    con.commit()
                    con.close()
                    tree1()
                    #preprocess+++++++++++++++++++++++++++++++++++++++++
                    i=se1.get()
                    pn=se2.get()
                    qty=se3.get()
                    ra=se4.get()
                    qty=int(qty)
                    ra=float(ra)
##
                        
                    tr=qty*ra#processing total rate

                    qty=str(qty)#reshape both qty & ra
                    ra=str(ra)
                    #processed
                    tup=(i,pn,qty,ra,tr)
                    print("%%%",tup)
                    try:
                        con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                        database="temp_cus")
                        cur=con.cursor()
                        sql="insert into temp_stock(pid,proname,qty,rate,totalrate) values(%s,%s,%s,%s,%s);"
                        cur.execute(sql,tup)
                        con.commit()
                        con.close()
                    except mysql.connector.errors.IntegrityError as ier:
                        con.close()
                        adpr=int(se3.get())
                        tup=(i,)
                        con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                        database="temp_cus")
                        cur=con.cursor()
                        sql="select qty from temp_stock where pid= %s"
                        cur.execute(sql,tup)
                        pqty=cur.fetchall()
                        con.close()
                        

                        pqty=pqty[-1]
                        pqty=int(pqty[-1])
                        cqty=pqty+adpr
                        try:
                            con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                            database="temp_cus")
                            sleep(3)
                            print(tr)
                            tr=cqty*tr
                            print(cqty)
                            print(tr)
                            tup=(cqty,tr,i)
                            cur=con.cursor()
                            sql="update temp_stock set qty=%s , totalrate= %s where pid=%s ;"
                            cur.execute(sql,tup)
                            con.commit()
                            con.close()
                            si("success","Successfully UPDATED")
                        except Exception as err:
                            print("your error is",err)
                    
            def tree2():    
                myTree1=ttk.Treeview(tab,height=15)
                myTree1['columns']=("","Customer ID","Customer Name","Phone NO","Email ID")
                myTree1.column('#0',width=0,stretch=NO)
                #1st column always as empty
                #stretch=NO means it will remove the 0th column 
                myTree1.column("#1",width=130)
                myTree1.column("#2",width=130)
                myTree1.column("#3",width=130)
                myTree1.column("#4",width=130)
                #in above code we are defining the column 1st then mention the headings below
                myTree1.heading("#0",text="")# 1st column always empty
                myTree1.heading("#1",text="Customer ID")
                myTree1.heading("#2",text="Customer Name")
                myTree1.heading("#3",text="Phone NO")
                myTree1.heading("#4",text="Email ID")

                #Dummy Records
                #myTree1.insert("",index=0,values=(1,"Krish","Tirupur","9994974215","krishleesya@gmail.com"))
                #add multiple records using for loop
                con=mysql.connector.connect(host="localhost",user="root",password="@angu1221",
                                                database="stockdp")
                cur=con.cursor()
                sql="select * from customer;"
                cur.execute(sql)
                row=cur.fetchall()
                
                con.close()
                self.sno=1
                
                for i in row:
                    myTree1.insert("",index="end",iid=self.sno,values=(i[0],i[1],i[2],i[3]),tags=("even",))
                    self.sno+=1
                    
                myTree1.tag_configure("low",font=("calibri",12,"bold"),background="red",foreground="white")
                myTree1.tag_configure("high",font=("calibri",12,"bold"),background="green",foreground="white")
                myTree1.tag_configure("even",font=("calibri",12,"bold"),background="white",foreground="black")
                myTree1.place(x=525,y=350)
                def mybind2(e):
                    sel=myTree1.focus()
                    print(sel)
                    vls=myTree1.item(sel,"values")
                    print(vls)
                    
                    ce1.delete(0,END)
                    ce2.delete(0,END)
                    ce3.delete(0,END)
                    ce4.delete(0,END)
                    
                    ce1.insert(0,vls[0])
                    ce2.insert(0,vls[1])
                    ce3.insert(0,vls[2])
                    ce4.insert(0,vls[3])
                    
                myTree1.bind("<ButtonRelease-1>",mybind2)

            tree1()
            tree2()
            
            vbbt=customtkinter.CTkButton(tab,text="View Bill",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=billview)
            vbbt.place(x=350,y=170)    

            
            vbbt1=customtkinter.CTkButton(tab,text="Add product",text_color="black",
                                        width=85,fg_color="#FFEE4D",command=checkout)
            vbbt1.place(x=350,y=120)


        ang=customtkinter.CTkToplevel(par)
        ang.geometry("1350x750")
        ang.title("Mainpage")
        mf1=customtkinter.CTkFrame(ang,width=1400,height=20,fg_color="#fbaccf")
        mf1.place(x=0,y=0)
        scaling_optionmenu = customtkinter.CTkOptionMenu(mf1,
                            values=["80%", "90%", "100%", "110%", "120%"],width=10,height=20,
                            fg_color="#fbaccf",text_color="black",button_hover_color="#fbaccf"
                            ,command=change_scaling_event)
        scaling_optionmenu.place(x=0,y=0)
         
        f1=customtkinter.CTkFrame(ang,width=300,height=700,fg_color="black")
        f1.place(x=0,y=20)
        l1=customtkinter.CTkLabel(f1,text="WELCOME",font=("Constantia",15)
                                                  ,text_color="white")
        l1.place(relx=0.5,rely=0.02,anchor="center")
#------------------------end of ctk design---------------------------------
#----------------------------buttons--------------------------
        l2=customtkinter.CTkLabel(f1,text="STOCK DETAILS",font=("Constantia",15)
                                                  ,text_color="white")
        l2.place(relx=0.5,rely=0.1,anchor="center")

        b1=customtkinter.CTkButton(f1,text="Add product",command=product)
        b1.place(x=70,y=100)
        b2=customtkinter.CTkButton(f1,text="Update",command=update)
        b2.place(x=70,y=150)
        b3=customtkinter.CTkButton(f1,text="Delete",command=delete)
        b3.place(x=70,y=200)
        b4=customtkinter.CTkButton(f1,text="Overall view",command=table)
        b4.place(x=70,y=250)

        l3=customtkinter.CTkLabel(f1,text="STOCK BILLS",font=("Constantia",15)
                                                  ,text_color="white")
        l3.place(x=90,y=350)
        
        b5=customtkinter.CTkButton(f1,text="Calc Bill",command=create_bill)
        b5.place(x=70,y=400)

        b6=customtkinter.CTkButton(f1,text="Customer Add",command=cust)
        b6.place(x=70,y=450)
        
        print("yes")
        #ang.mainloop()


        
'''
a=Tk()
a.withdraw()
maincls(a)
'''




