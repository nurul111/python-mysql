from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.canvas = Canvas(width=500, height=500, bg='#005D5C')
        self.canvas.pack()
        i = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        #verifying Input
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0 or len(i.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(book_id,name,author,availability) values (%s,%s,%s,%s)",[i.get(),b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Book.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label
        Label(self, text='').pack()
        Label(self, text='Book Details',bg='#005D5C',fg='yellow',font=('Courier new', 20, 'bold')).place(x=160, y=50)
        Label(self, text='').pack()
        Label(self, text='Book ID:',bg='#005D5C',fg='white', font=('Courier new', 12, 'bold')).place(x=70, y=140)
        Entry(self, textvariable=i, width=30).place(x=200, y=142)
        Label(self, text='Book Name:',bg='#005D5C',fg='white', font=('Courier new', 12, 'bold')).place(x=70, y=185)
        Entry(self, textvariable=b, width=30).place(x=200, y=187)
        Label(self, text='Book Author:',bg='#005D5C',fg='white', font=('Courier new', 12, 'bold')).place(x=70, y=230)
        Entry(self, textvariable=c, width=30).place(x=200, y=232)
        Button(self, text="Submit",width=10,bg='#005D5C',fg='white',font=('Courier new',12,'bold'), command=b_q).place(x=220, y=280)
Add().mainloop()