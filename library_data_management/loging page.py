from tkinter import *
from tkinter import messagebox
import sys
import os
import mysql.connector
from mysql.connector import Error
py=sys.executable
from PIL import ImageTk,Image

#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 500)
        self.minsize(1200, 500)
        self.canvas = Canvas(width=1200, height=500,bg='#005D5C')
        self.canvas.pack()
        #self.configure(bg='gray')
        self.title("LIBRARY MANAGEMENT SYSTEM")
        self.img=ImageTk.PhotoImage(Image.open("C:\\Users\\nurul\\Downloads\\SeekPng.com_white-tree-png_519065.png"))
        self.canvas.create_image(0,240,anchor='center',image=self.img)

        self.img2=ImageTk.PhotoImage(Image.open("C:\\Users\\nurul\\Downloads\\SeekPng.com_white-tree-png_519065.png"))
        self.canvas.create_image(1200,250,anchor='center',image=self.img2)

        #verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='library',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user_id= %s AND password = %s ',(user,password))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():


            self.label = Label(self, text="LOGIN", bg = '#005D5C' , fg = 'yellow', font=("courier-new", 20))
            self.label.place(x=550, y=90)
            self.label1 = Label(self, text="User-Id" , bg = '#005D5C' , fg = 'white', font=("courier-new", 18,'bold'))
            self.label1.place(x=350, y=183)
            self.user_text = Entry(self, textvariable=self.a, width=45)
            self.user_text.place(x=480, y=190)
            self.label2 = Label(self, text="Password" , bg = '#005D5C' , fg = 'white', font=("courier-new", 18, 'bold'))
            self.label2.place(x=350, y=247)
            self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
            self.pass_text.place(x=480, y=255)
            self.butt = Button(self, text="Login",bg ='#005D5C',fg='white', font=('Courier-new',12,'bold'), width=10, command=chex).place(x=560, y=320)
            self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='#005D5C', fg='yellow', font=("courier-new", 20))
            self.label3.place(x=350, y=30)


        check()

Lib().mainloop()