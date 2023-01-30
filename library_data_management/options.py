from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
py=sys.executable
from PIL import ImageTk,Image

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.configure(bg='#005D5C')
        self.canvas = Canvas(width=1366, height=768, bg='#005D5C')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEM')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
        #self.img1=ImageTk.PhotoImage(Image.open("C:\\Users\\nurul\\Downloads\\pexels-vlad-chețan-1595655.jpg"))
        #self.canvas.create_image(1000,900,anchor='center',image=self.img1)
        #self.img2=ImageTk.PhotoImage(Image.open('C:\\Users\\User\\Pictures\\tree3.jpg'))
        #self.canvas.create_image(1290,330,anchor='center',image=self.img2)

        #calling scripts
        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def a_b():
            os.system('%s %s' % (py, 'Add_Book.py'))

        def r_b():
            os.system('%s %s' % (py, 'remove_book.py'))

        def r_s():
            os.system('%s %s' % (py, 'Remove_student.py'))

        def ib():
            os.system('%s %s' % (py, 'Book_Issuing.py'))

        def ret():
            os.system('%s %s' % (py, 'Return_Book.py'))

        def seb():
            os.system('%s %s' % (py,'Book.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'main.py'))



        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"
        def add_user():
            os.system('%s %s' % (py, 'Reg.py'))
        def rem_user():
            os.system('%s %s' % (py, 'Rem.py'))
        def sest():
            os.system('%s %s' % (py,'student.py'))

        #creating table

        self.listTree = ttk.Treeview(self,height=10,columns=('Student','Book','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=160,minwidth=100,anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=180, minwidth=125,anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=180, minwidth=125, anchor='center')
        self.listTree.place(x=193,y=320)
        self.vsb.place(x=1120,y=320,height=225)
        self.hsb.place(x=194,y=551,width=922)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        list1 = Menu(self)
        list1.add_command(label="Add", command=a_s)
        list1.add_command(label="Search", command=sest)
        list1.add_command(label='Remove',command=r_s)

        list2 = Menu(self)
        list2.add_command(label='logout',command=log)

        list3 = Menu(self)
        list3.add_command(label = "Add User",command = add_user)
        list3.add_command(label = "Remove User",command = rem_user)

        list4 = Menu(self)
        list4.add_command(label = 'Add',command = a_b)
        list4.add_command(label = 'Search',command = seb)
        list4.add_command(label = 'Remove',command = r_b)
        list4.add_command(label = 'Issue',command = ib)
        list4.add_command(label = 'Return',command = ret)


        self.mymenu.add_cascade(label ='Admin Tools', menu = list3)
        self.mymenu.add_cascade(label='Student', menu = list1)
        self.mymenu.add_cascade(label = 'Book',menu = list4)
        self.mymenu.add_cascade(label = 'Logout',menu = list2)


        self.config(menu=self.mymenu)

        def ser():
            if(len(self.a.get())==0):
                messagebox.showinfo("Error", "Empty Field!")
            else:

                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='library',
                                                   user='root',
                                                   password='')
                    mycursor = conn.cursor()
                    change = self.a.get()
                    mycursor.execute("Select bi.student_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi, student s,book b where s.student_id = bi.student_id and b.book_id = bi.book_id and s.student_id = %s",[change])
                    pc = mycursor.fetchall()
                    print(pc)
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
                except Error:
                    #print(Error)
                    messagebox.showerror("Error","Something Goes Wrong")
        def ent():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    book = int(self.bookid.get())
                    self.myCursor.execute("Select bi.book_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi, student s, book b where s.student_id = bi.student_id and b.book_id = bi.book_id and b.book_id = %s",[book])
                    self.pc = self.myCursor.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued")
                except Error:
                    messagebox.showerror("Error", "Something Goes Wrong")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='library',
                                               user='root',
                                               password='')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm","Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Reg.py'))
                else:
                    #label and input box
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM',fg='yellow',bg="#005D5C" ,font=('Courier new', 30, 'bold'))
                    self.label3.place(x=350, y=40)
                    self.label4 = Label(self, text="STUDENT ID",fg='white',bg="#005D5C", font=('Courier new', 18, 'bold'))
                    self.label4.place(x=190, y=150)
                    Entry(self, textvariable=self.a, width=90).place(x=360, y=155)
                    self.srt = Button(self, text='Search', width=15,bg='#005D5C',fg='white', font=('Courier new', 12,'bold'),command = ser).place(x=950, y=150)
                    self.label5 = Label(self, text="BOOK ID",fg='white',bg="#005D5C", font=('Courier new', 18, 'bold'))
                    self.label5.place(x=190, y=190)
                    self.bookid = Entry(self, textvariable=self.b, width=90)
                    self.bookid.place(x=360, y=195)
                    self.brt = Button(self, text='Find', width=15,bg='#005D5C',fg='white', font=('Courier new', 12,'bold'),command = ent).place(x=950, y=190)
                    self.label6 = Label(self, text="INFORMATION DETAILS",bg="#005D5C",fg='white',  font=('Courier new', 15, 'underline', 'bold'))
                    self.label6.place(x=520, y=250)
                    #self.button = Button(self, text='Search Student', width=20, font=('Courier new', 12,'bold'), command=sest).place(x=195,y=250)
                    #self.button = Button(self, text='Search Book', width=20, font=('Courier new', 12,'bold'), command=seb).place(x=420,y=250)
                    #self.brt = Button(self, text="Issue Book", width=20, font=('Courier new', 12,'bold'), command=ib).place(x=645, y=250)
                    #self.brt = Button(self, text="Return Book", width=20, font=('Courier new', 12,'bold'), command=ret).place(x=870, y=250)
                    #self.brt = Button(self, text="LOGOUT", width=15,bg="red", font=('Courier new', 12,'bold'), command=log).place(x=1150, y=105)
            except Error:
                messagebox.showerror("Error", "Something Goes Wrong")
        check()

MainWin().mainloop()
