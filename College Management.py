from Tkinter import *
import MySQLdb
import os

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="college")        # name of the data base

# you must create a Cursor object. It will let you execute all the queries you need
cur = db.cursor()

def Login():
    global nameEL
    global pwordEL # globals 
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login User') # This makes the window title 'login user'
 
    intruction = Label(rootA, text='Please Login\n') # labels to tell us what they do
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login as Admin', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(row=3, column=1, columnspan=2, sticky=W)
 
    rmuser = Button(rootA, text='Login as Student', command=Student) # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(row=3, column=3,columnspan=2)
    rootA.mainloop()
 
def CheckLogin():
     
    if nameEL.get() == "admin" and pwordEL.get() == "admin": # Checks to see if you entered the correct data.
        Admin()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
        Login()

def Admin():
    os.system('admin.py')
def Student():
    os.system('student.py')

Login()
