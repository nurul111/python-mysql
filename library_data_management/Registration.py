from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg='#005D5C')
        self.canvas.pack()
        #creating variables Please chech carefully
        u = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                                    database='library',
                                                    user='root',
                                                    password='')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,password) values (%s,%s)",[u.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
        #label and input
        Label(self, text='User Details', bg='#005D5C', fg='yellow', font=('Courier new', 25, 'bold')).place(x=130, y=22)
        Label(self, text='Username:', bg='#005D5C',fg = 'white', font=('Courier new', 15, 'bold')).place(x=70, y=110)
        Entry(self, textvariable=u, width=30).place(x=200, y=114)
        Label(self, text='Password:', bg='#005D5C',fg='white', font=('Courier new', 15, 'bold')).place(x=70, y=196)
        Entry(self, textvariable=p, width=30).place(x=200, y=199)
        Button(self, text="Submit", width=10,bg='#005D5C',fg='white',font=('Courier new',12,'bold') ,command=insert).place(x=198, y=270)
reg().mainloop()