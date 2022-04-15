from tkinter import*
from tkinter import ttk,messagebox
import pymysql

class customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Loan Management System")
        self.root.geometry('1350x720+0+0')
        title= Label(self.root,text="Loan Management System",font=('times new rommon',40,'bold'),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)

        # Variables

        self.loanId=StringVar()
        self.name=StringVar()
        self.mob=StringVar()
        self.aadhar=StringVar()
        self.add=StringVar()
        self.pin=StringVar()
        self.mpay=StringVar()
        self.tpay=StringVar()
        self.rate=StringVar()
        self.years=StringVar()
        self.amount=StringVar()
        self.time=StringVar()

        # Details Frame

        Detail_F=Frame(self.root,bd=4,relief=RIDGE,bg='powderblue')
        Detail_F.place(x=10,y=90,width=520,height=620)

        lbl_id=Label(Detail_F,text='Loan Id',font=('times new rommon',15,'bold'))
        lbl_id.grid(row=0,column=0,padx=20,pady=10,sticky='w')
        txt_id=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.loanId)
        txt_id.grid(row=0,column=1)

        lbl_name=Label(Detail_F,text='Full Name',font=('times new rommon',15,'bold'))
        lbl_name.grid(row=1,column=0,padx=20,pady=10,sticky='w')
        txt_name=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.name)
        txt_name.grid(row=1,column=1)

        lbl_mob=Label(Detail_F,text='Mobile No.',font=('times new rommon',15,'bold'))
        lbl_mob.grid(row=2,column=0,padx=20,pady=10,sticky='w')
        txt_mob=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.mob)
        txt_mob.grid(row=2,column=1)

        lbl_aa=Label(Detail_F,text='Aadhar No.',font=('times new rommon',15,'bold'))
        lbl_aa.grid(row=3,column=0,padx=20,pady=10,sticky='w')
        txt_aa=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.aadhar)
        txt_aa.grid(row=3,column=1)

        lbl_add=Label(Detail_F,text='Address',font=('times new rommon',15,'bold'))
        lbl_add.grid(row=4,column=0,padx=20,pady=10,sticky='w')
        txt_add=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.add)
        txt_add.grid(row=4,column=1)

        lbl_pin=Label(Detail_F,text='PinCode',font=('times new rommon',15,'bold'))
        lbl_pin.grid(row=5,column=0,padx=20,pady=10,sticky='w')
        txt_pin=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.pin)
        txt_pin.grid(row=5,column=1)

        lbl_amount=Label(Detail_F,text='Amount Of Loan',font=('times new rommon',15,'bold'))
        lbl_amount.grid(row=6,column=0,padx=20,pady=10,sticky='w')
        txt_amount=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.amount)
        txt_amount.grid(row=6,column=1)

        lbl_time=Label(Detail_F,text='Number Of Years',font=('times new rommon',15,'bold'))
        lbl_time.grid(row=7,column=0,padx=20,pady=10,sticky='w')
        txt_time=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.time)
        txt_time.grid(row=7,column=1)

        lbl_rate=Label(Detail_F,text='Interest Rate',font=('times new rommon',15,'bold'))
        lbl_rate.grid(row=8,column=0,padx=20,pady=10,sticky='w')
        txt_rate=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.rate)
        txt_rate.grid(row=8,column=1,pady=10,sticky='w')

        lbl_Mp=Label(Detail_F,text='Monthly Payment',font=('times new rommon',15,'bold'))
        lbl_Mp.grid(row=9,column=0,padx=20,pady=10,sticky='w')
        txt_Mp=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.mpay)
        txt_Mp.grid(row=9,column=1)

        lbl_tp=Label(Detail_F,text='Total Payment',font=('times new rommon',15,'bold'))
        lbl_tp.grid(row=10,column=0,padx=20,pady=10,sticky='w')
        txt_tp=Entry(Detail_F,font=('times new rommon',18,'bold'),bd=3,relief=GROOVE,textvariable=self.tpay)
        txt_tp.grid(row=10,column=1)

        RFrame=Frame(self.root,bd=4,relief=RIDGE)
        RFrame.place(x=535,y=90,width=800,height=520)

        yscroll=Scrollbar(RFrame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(RFrame,columns=('empid','name','years','rate','Mpayment','Tpayment','mobile'),yscrollcommand=yscroll)
        yscroll.pack(side=RIGHT,fill=Y)
        yscroll.config(command=self.employee_table.yview)
        self.employee_table.heading('empid',text='Loan Id')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('years',text='Number Of Years')
        self.employee_table.heading('rate',text='Interest Rate')
        self.employee_table.heading('Mpayment',text='Monthly Payment')
        self.employee_table.heading('Tpayment',text='Total Payment')
        self.employee_table.heading('mobile',text='Mobile No.')
        self.employee_table['show']='headings'

        self.employee_table.column('empid',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('years',width=100)
        self.employee_table.column('rate',width=100)
        self.employee_table.column('Mpayment',width=100)
        self.employee_table.column('Tpayment',width=100)
        self.employee_table.column('mobile',width=100)
        
        self.employee_table.pack(fill=BOTH,expand=1)

        self.fetch()
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)

        #Button

        btn_Frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_Frame.place(x=535,y=610,width=810,height=100)

        btn1=Button(btn_Frame,text='Add record',font='arial 15 bold',width=9,bg='lime',fg='blue',command=self.addrecord)
        btn1.grid(row=0,column=0,padx=10,pady=10)

        btn2=Button(btn_Frame,text='Update',font='arial 15 bold',bg='lime',fg='blue',width=9,command=self.update)
        btn2.grid(row=0,column=1,padx=10,pady=10)

        btn3=Button(btn_Frame,text='Delete',font='arial 15 bold',bg='lime',fg='blue',width=9,command=self.delete)
        btn3.grid(row=0,column=2,padx=10,pady=10)

        btn4=Button(btn_Frame,text='Reset',font='arial 15 bold',bg='lime',fg='blue',width=9,command=self.reset)
        btn4.grid(row=0,column=3,padx=10,pady=10)

        btn5=Button(btn_Frame,text='Exit',font='arial 15 bold',bg='lime',fg='blue',width=9,command=self.exit)
        btn5.grid(row=0,column=4,padx=10,pady=10)

# Functions

    def total(self):
        p=int(self.amount.get())
        r=int(self.rate.get())
        y=int(self.years.get())

        t=(p*r*y*12)/100
        m=(p+t)/(y*12)
        self.mpay.set(str(round(m,2)))
        self.tpay.set(str(p+t))

    def addrecord(self):
       if self.loanId.get()=='':
           messagebox.showerror('Error','Customer details are must')
       else:
            con=pymysql.connect(host='localhost',user='root',password='',database='emp')
            cur=con.cursor()
            cur.execute("Select * from customer")
            rows=cur.fetchall()
            for row in rows:
                if row[0]==self.loanId.get():
                    messagebox.showerror('Error','Duplicate entry not allowed')
                    return
                
            cur.execute("Insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.loanId.get(),
                                                                               self.name.get(),
                                                                               self.years.get(),
                                                                               self.rate.get(),
                                                                               self.mpay.get(),
                                                                               self.tpay.get(),
                                                                               self.mob.get(),
                                                                               self.aadhar.get(),
                                                                               self.add.get(),
                                                                               self.pin.get(),
                                                                               self.amount.get()
                                                                                ))

            con.commit()
            self.fetch()
            con.close()

    def fetch(self):
         con=pymysql.connect(host='localhost',user='root',password='',database='emp')
         cur=con.cursor()
         cur.execute("Select * from customer")
         rows=cur.fetchall()
         if len(rows)!=0:
             self.employee_table.delete(*self.employee_table.get_children())
             for row in rows:
                self.employee_table.insert('',END,Values=row)
         con.commit()
         con.close()

    def get_cursor(self,ev):
        cur_row=self.employee_table.focus()
        content=self.employee_table.item(cur_row)
        row=content['values']
        self.loanId.set(row[0])
        self.name.set(row[1])
        self.years.set(row[2])
        self.rate.set(row[3])
        self.mpay.set(row[4])
        self.tpay.set(row[5])
        self.mob.set(row[6])
        self.aadhar.set(row[7])
        self.add.set(row[8])
        self.pin.set(row[9])
        self.amount.set(row[10])

    def update(self):
        if self.loanId.get()=='':
            messagebox.showerror('Error','Input information for update')
        else:
            con=pymysql.connect(host='localhost',user='root',password='',database='emp')
            cur=con.cursor()
            cur.execute("Update customer set Name=%s,Year=%s,Rate=%s,Monthly_Payment=%s,Total_Payment=%s,MobileNumber=%s,AadharNumber=%s,Pincode=%s,Amount=%s where Loan_Id=%s",(self.name.get(),
                        self.years.get(),
                        self.rate.get(),
                        self.mpay.get(),
                        self.tpay.get(),
                        self.mpb.get(),
                        self.aadhar.get(),
                        self.add.get(),
                        self.pin.get(),
                        self.amount.get(),
                        self.loanId.get()
                         ))



            messagebox.showinfo('info',f'Recor{self.loanId.get()} Updated Successfully')
            con.commit()
            con.close()
            self.fetch()
            self.reset()

    def delete(self):
        if self.loanId.get()=='':
            messagebox.showerror('Error','Input Loan Id To Delete The Record')
        else:
             con=pymysql.connect(host='localhost',user='root',password='',database='emp')
             cur=con.cursor()
             cur.execute("Delete form customer where Loan_Id=%s",self.loanId.get())
             con.commit()
             con.close()
             self.fetch()
             self.reset()


    def reset(self):
        self.loanId.set('')
        self.name.set('')
        self.mob.set('')
        self.aadhar.set('')
        self.add.set('')
        self.pin.set('')
        self.amount.set('')
        self.years.set('')
        self.rate.set('')
        self.mpay.set('')
        self.tpay.set('')
        
    def exit(self):
        if messagebox.askyesno('Exit','Do you reallu want to exit'):
            root.destroy()

            

root=Tk()
obj=customer(root)
root.mainloop()
