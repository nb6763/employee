from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

import mysql.connector as ms # imported mysql.connector
connection = ms.connect(host='localhost',user='root',password='Jatin@123',database='employee')
mycursor = connection.cursor() # created cursor


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="brown")

        self.bg=ImageTk.PhotoImage(file="IMG_0019.JPG")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1, relwidth=1)
        self.left = ImageTk.PhotoImage(file="img_1.png")
        left = Label(self.root, image=self.left).place(x=200, y=100, width=400, height=500)
        heading=Label(self.root,text="Welcome to our employee portal",font=("times new roman",30,'bold')).place(x=300, y=30)


        frame1=Frame(self.root,bg="white")
        frame1.place(x=500,y=100,height=500,width=700)
        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white", fg="blue").place(x=50,y=30)


        Fname=Label(frame1,text="First Name",font=("times new roman",12,"bold"),bg="white").place(x=50,y=80)
        self.Fname_entry = Entry(frame1, font=("times new roman", 12, "bold"),bg="lightgrey")
        self.Fname_entry.place(x=50, y=100, width=300)

        lname = Label(frame1, text="Last Name", font=("times new roman", 12, "bold"), bg="white").place(x=370, y=80)
        self.lname_entry = Entry(frame1, font=("times new roman", 12, "bold"),bg="lightgrey" )
        self.lname_entry.place(x=370, y=100, width=300)

        CNO = Label(frame1, text="Contact Number", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=150)
        self.CNO_entry = Entry(frame1, font=("times new roman", 12, "bold"),bg="lightgrey" )
        self.CNO_entry.place(x=50, y=180, width=300 )

        Email = Label(frame1, text="Email", font=("times new roman", 12, "bold"), bg="white").place(x=370, y=150)
        self.Email_entry = Entry(frame1, font=("times new roman", 12, "bold"),bg="lightgrey" )
        self.Email_entry.place(x=370, y=180, width=300)

        Question = Label(frame1, text="Select a question", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=200)
        self.combo=ttk.Combobox(frame1, font=("times new roman", 12, "bold"),state='readonly', justify=CENTER)
        self.combo['values']=["select","your favorite pet", "your husbands name", "your brother name"]
        self.combo.place(x=50, y=220, width=300)
        self.combo.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 12, "bold"), bg="white").place(x=370, y=200)
        self.answerentry = Entry(frame1, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.answerentry.place(x=370, y=220, width=300)

        password = Label(frame1, text="Password", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=250)
        self.passwordentry = Entry(frame1, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.passwordentry.place(x=50, y=270, width=300)

        cpwd = Label(frame1, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white").place(x=370, y=250)
        self.cpwdentry = Entry(frame1, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.cpwdentry.place(x=370, y=270, width=300)

        self.varcheck=IntVar()
        checkbox=Checkbutton(frame1, text="I agree the terms and conditions",variable=self.varcheck, onvalue=1,offvalue=0).place(x=50,y=300)
        btn_register=Button(frame1,text="Register Here",font=("times new roman", 15,'bold'), cursor="hand2",command=self.register_data).place(x=300,y=330,width=200, height=40)
        login_btn=Button(self.root,text="Login",font=("times new roman", 15,'bold'),cursor="hand2",bd=1,command=self.login_data).place(x=300,y=500, width=80, height=40)

        delete=Button(self.root,text="Delete",font=("times new roman", 15,'bold'),cursor="hand2",bd=1,command=self.delete_data).place(x=300,y=300, width=80, height=40)

    def register_data(self):
        print("FIRST NAME:",self.Fname_entry.get(),"LAST NAME:",self.lname_entry.get())
        print("CONTACT NUMBER:",self.CNO_entry.get())
        print("EMAIL ID",self.Email_entry.get())
        print("YOUR QUESTION:",self.combo.get(),"YOUR ANSWER",self.answerentry.get())
        print("YOUR PASSWORD",self.passwordentry.get())
        print("CONFIRMED PASSWORD",self.cpwdentry.get())




        mycursor.execute("select * from employee_details where Email_Id = '{}';".format(self.Email_entry.get()))
        row = mycursor.fetchone()
        if row!=None:
            messagebox.showerror("error", "Email Id already exits", parent=self.root)
        else:
            if self.Fname_entry.get()=="":
                messagebox.showerror("error","enter the first name",parent=self.root)
            elif self.lname_entry.get()=="":
                messagebox.showerror("error","enter the Last name",parent=self.root)
            elif self.CNO_entry.get()=="":
                messagebox.showerror("error","enter the contact number",parent=self.root)
            elif self.Email_entry.get()=="":
                messagebox.showerror("error","enter the email",parent=self.root)
            elif self.combo.get()=="" or self.combo.get()=="select":
                messagebox.showerror("error","select a question",parent=self.root)
            elif self.answerentry.get()=="":
                messagebox.showerror("error","Please write an answer",parent=self.root)
            elif self.passwordentry.get() == "":
                messagebox.showerror("error", "enter the first name", parent=self.root)
            elif self.cpwdentry.get()=="":
                messagebox.showerror("error","enter the first name",parent=self.root)
            elif self.passwordentry.get()!=self.cpwdentry.get():
                messagebox.showerror("error","password and confirmed password are not same",parent=self.root)
            elif self.varcheck.get()==0:
                messagebox.showerror("error", "please agree the terms and conditions", parent=self.root)
            else:
                messagebox.showinfo("sucess","Registeration successful",parent=self.root)
                mycursor.execute("insert into  employee_details values('{}','{}','{}','{}','{}','{}','{}');".format(
                    self.Fname_entry.get(), self.lname_entry.get(), self.CNO_entry.get(), self.Email_entry.get(),
                    self.combo.get(), self.answerentry.get(), self.passwordentry.get(), self.cpwdentry.get()))
                mycursor.execute("commit;")
            frame1.place_forget()
            self.Fname_entry.destroy()
            self.lname_entry.destroy()
            self.CNO_entry.destroy()
            self.Email_entry.destroy()
            self.combo.destroy()
            self.answerentry.destroy()
            self.passwordentry.destroy()
            self.cpwdentry.destroy()

    def delete_data(self):
        frame5 = Frame(self.root, bg="white")
        frame5.place(x=500, y=100, height=500, width=700)
        title = Label(frame5, text="DELETE A RECORD", font=("times new roman", 20, "bold"), bg="lightblue", fg="blue").place(x=50, y=30)

        Email = Label(frame5, text="Email", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=150)
        self.Email2_entry = Entry(frame5, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.Email2_entry.place(x=150, y=150, width=300)

        onclickdel=Button(frame5,text="delete", font=("times new roman", 15,'bold'),cursor="hand2",bd=1,command=self.delete).place(x=150,y=250,height=100,width=100)
    def delete(self):
        query = "delete from employee_details where Email_Id = '{}';".format(self.Email2_entry.get())
        mycursor.execute(query)
        mycursor.execute("commit;")

    def login_data(self):
        frame2 = Frame(self.root, bg="white")
        frame2.place(x=500, y=100, height=500, width=700)
        title = Label(frame2, text="login", font=("times new roman", 20, "bold"), bg="lightblue", fg="blue").place(x=50, y=30)

        Email = Label(frame2, text="Email", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=150)
        self.Email1_entry = Entry(frame2, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.Email1_entry.place(x=150, y=150, width=300)

        password = Label(frame2, text="Password", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=180)
        self.password1entry = Entry(frame2, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.password1entry.place(x=150, y=180, width=300)

        submit = Button(frame2, text="submit", font=("times new roman", 15, 'bold'), cursor="hand2", bd=1,command=self.submit_data).place(x=600, y=400, width=80, height=40)

    def submit_data(self):
        mycursor.execute("select Email_Id from employee_details where Email_Id = '{}';".format(self.Email1_entry.get()))
        email1= mycursor.fetchone()

        mycursor.execute("select password from employee_details where password = '{}';".format(self.password1entry.get()))
        password1 = mycursor.fetchone()



        if email1!=None and password1!=None :
            messagebox.showinfo("sucess", "Login successful", parent=self.root)

            frame3 = Frame(self.root, bg="white")
            frame3.place(x=500, y=100, height=500, width=700)
            title = Label(frame3, text="Employee details", font=("times new roman", 20, "bold"), bg="white",
                          fg="blue").place(x=50, y=30)

            mycursor.execute("select First_Name from employee_details where Email_Id = '{}';".format(self.Email1_entry.get()))
            fn = mycursor.fetchone()
            fn= fn[0]

            Fnamedetails = Label(frame3, text="First Name: "+fn ,font=("times new roman", 12, "bold"), bg="white").place(x=50, y=80)

            mycursor.execute("select Last_Name from employee_details where Email_Id = '{}';".format(self.Email1_entry.get()))
            ln = mycursor.fetchone()
            ln = ln[0]

            lnamedetails = Label(frame3, text="Last Name: " + ln, font=("times new roman", 12, "bold"),
                                 bg="white").place(x=50, y=110)

            mycursor.execute("select Contact_number from employee_details where Email_Id = '{}';".format(self.Email1_entry.get()))
            cno = mycursor.fetchone()
            cno = cno[0]

            contactdetails = Label(frame3, text="Contact Number:  " + cno, font=("times new roman", 12, "bold"),
                                 bg="white").place(x=50, y=140)

            mycursor.execute("select Email_ID from employee_details where Email_Id = '{}';".format(self.Email1_entry.get()))
            emid = mycursor.fetchone()
            emid = emid[0]

            emaildetails = Label(frame3, text="Email Id :  " + emid, font=("times new roman", 12, "bold"),bg="white").place(x=50, y=170)

            updt_details=Button(frame3, text="UPDATE", font=("times new roman", 15, 'bold'), cursor="hand2", bd=1,command=self.update_details).place(x=600, y=400, width=80, height=40)


        else:
                messagebox.showerror("Error", "You are not regsitered", parent=self.root)


    def update_details(self):
        frame4 = Frame(self.root, bg="white")
        frame4.place(x=500, y=100, height=500, width=700)
        title = Label(frame4, text="update employee details", font=("times new roman", 20, "bold"), bg="white",fg="blue").place(x=50, y=30)

        fnamedetailsup = Label(frame4, text="First Name: ", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=80)
        self.fnupdate= Entry(frame4, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.fnupdate.place(x=150, y=80, width=300)

        lnamedetailsup = Label(frame4, text="Last Name: ", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=110)
        self.lnupdate = Entry(frame4, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.lnupdate.place(x=150, y=110, width=300)

        cndetailsup = Label(frame4, text="Contact number: ", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=130)
        self.cnupdate = Entry(frame4, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.cnupdate.place(x=150, y=130, width=300)

        psnamedetailsup = Label(frame4, text="Password: ", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=150)
        self.psupdate = Entry(frame4, font=("times new roman", 12, "bold"), bg="lightgrey")
        self.psupdate.place(x=150, y=150, width=300)


        update = Button(frame4, text="update", font=("times new roman", 15, 'bold'), cursor="hand2", bd=1,command=self.update).place(x=600, y=400, width=80, height=40)
        back_to_login=Button(frame4, text="Back to login", font=("times new roman", 15, 'bold'), cursor="hand2", bd=1,command=self.login_data).place(x=300, y=400, width=200, height=40)


    def update(self):
        mycursor.execute("update employee_details set First_Name = '{}',Last_Name= '{}',Contact_number = '{}',password='{}' where Email_Id = '{}';".format(self.fnupdate.get(),self.lnupdate.get(),self.cnupdate.get(),self.psupdate.get(),self.Email1_entry.get()))
        mycursor.execute("commit;")



root=Tk()
obj=Register(root)
root.mainloop()