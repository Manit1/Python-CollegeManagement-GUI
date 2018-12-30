from Tkinter import *
import MySQLdb
import os
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="college")        # name of the data base

# you must create a Cursor object. It will let you execute all the queries you need
cursor = db.cursor()

root= Tk()
topframe=Frame(root,width=1600,height=150,bg="yellow")
topframe.pack()
bottomframe=Frame(root,width=1600,height=650)
bottomframe.pack()
scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

y=Canvas(topframe,width=1600,height=150,background="#2E86C1")
y.pack(side=LEFT,expand=YES,fill=BOTH)
c=Canvas(bottomframe,width=1600,height=650,background="#2E86C1")
c.pack(side=LEFT,expand=YES,fill=BOTH)
root.title("College management")
root.geometry("1600x800+0+0")
gif1 = PhotoImage(file = 'HMR.gif')
y.create_image(0, 0, image = gif1, anchor = NW)
def home():
   c.delete("all")
   c.create_text(600,100,font=("Callibri",20),text="College Information(HMRITM)")
   c.create_text(600,200,font=("Arial",16),text="This is a Python based project which gives\n information about our college HMRITM")

home()

def ec():
   os.system('ecdb.py')   

def hod():
   c.delete("all")
   c.create_text(200,25,font=("Callibri",20),text="HEAD OF DEPARTMENT")
   c.create_text(200,90,font=("Arial",16),text="\nCSE - Dr. Ravinder Kumar\nECE - Dr. Avadhesh Kumar Sharma\nEEE - Dr. Pawan Kumar Sharma")

def ee():
   os.system('eedb.py')   

def cs():
   os.system('csedb.py')   
def About():
   c.delete("all")
   c.create_text(500,200,font=("Arial",16),text="\nThis GUI is made for learning")

def made():
   c.delete("all")
   c.create_text(500,200,font=("Arial",16),text="\n1.Chirag Malhotra\n2.Dhiren Kathpalia\n3.Manit Malhotra\n4.Mohak Chaudhary\n5.Himanshu Kumar")


homebutton= Button(topframe,text="HOME",fg="blue",command=home)
ecbutton= Button(topframe,text="ECE",fg="blue",command=ec)
eebutton= Button(topframe,text="EEE",fg="blue",command=ee)
csbutton= Button(topframe,text="CSE",fg="blue",command=cs)
hodbutton= Button(topframe,text="HOD",fg="blue",command=hod)
homebutton.configure(relief=FLAT)
ecbutton.configure(relief=FLAT)
eebutton.configure(relief=FLAT)
csbutton.configure(relief=FLAT)
hodbutton.configure(relief=FLAT)

homebutton_window = y.create_window(500, 100, anchor=W, window=homebutton)
ecbutton_window = y.create_window(560, 100, anchor=W, window=ecbutton)
eebutton_window = y.create_window(680, 100, anchor=W, window=eebutton)
csbutton_window = y.create_window(620, 100, anchor=W, window=csbutton)
hodbutton_window = y.create_window(720, 100, anchor=W, window=hodbutton)

m = Menu(root)
root.config(m=m)
filemenu = Menu(m)
m.add_cascade(label="File", m=filemenu)
filemenu.add_command(label="GUI Made BY-", command=made)
filemenu.add_command(label="Exit", command=root.destroy)

helpmenu = Menu(m)
m.add_cascade(label="Help", m=helpmenu)
helpmenu.add_command(label="About...", command=About)
db.close()
root.mainloop()
