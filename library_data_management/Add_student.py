from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=400, bg='#005D5C')
        self.canvas.pack()
        i = StringVar()
        n = StringVar()
        p = StringVar()
        a = StringVar()
        #verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(i.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your ID")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    id = i.get()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    self.myCursor.execute("Insert into student(student_id,name,phone_number,address) values (%s,%s,%s,%s)",[id,name1,pn1,add1])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                        self.destroy()
                        self.myCursor.close()
                        self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        #Label(self, text='Student Details',bg='#005D5C', fg='yellow', font=('Courier new', 25, 'bold')).pack()
        Label(self,text='Id:',bg='#005D5C',fg = 'white',font=('Courier new', 15, 'bold')).place(x=70, y=40)
        Entry(self, textvariable=i, width=30).place(x=230, y=42)
        Label(self, text='Name:',bg='#005D5C',fg = 'white', font=('Courier new', 15, 'bold')).place(x=70, y=92)
        Entry(self, textvariable=n, width=30).place(x=230, y=94)
        Label(self, text='Phone Number:',bg='#005D5C',fg = 'white', font=('Courier new', 15, 'bold')).place(x=70, y=140)
        Entry(self, textvariable=p, width=30).place(x=230, y=142)
        Label(self, text='Address:',bg='#005D5C', fg = 'white',font=('Courier new', 15, 'bold')).place(x=70, y=190)
        Entry(self, textvariable=a, width=30).place(x=230, y=192)
        Button(self, text="Submit",width = 15,bg='#005D5C',fg='white',font=('Courier new',12,'bold'),command=asi).place(x=230, y=250)

Add().mainloop()