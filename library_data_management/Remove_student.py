from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.maxsize(500, 200)
        self.minsize(500, 200)
        self.title("Remove student")
        self.canvas = Canvas(width=500, height=200, bg='#005D5C')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                                            database='library',
                                                            user='root',
                                                            password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from student where student_id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "Enter Student Id: ",bg='#005D5C',fg='white',font=('Courier new', 15, 'bold')).place(x = 30,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 250,y = 44)
        Button(self, text='Remove', width=15,bg='#005D5C',fg='white', font=('Courier new', 12,'bold'),command = ent).place(x=200, y = 120)



Rem().mainloop()