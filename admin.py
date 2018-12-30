from Tkinter import *
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="college")        # name of the data base
cur= db.cursor()

root = Tk()
topframe=Frame(root,width=1600,height=150)
topframe.pack()
bottomframe=Frame(root,width=1600,height=650)
bottomframe.pack()
scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

y=Canvas(topframe,width=1600,height=150,background="#2E86C1")
y.pack(side=LEFT,expand=YES,fill=BOTH)
x=Canvas(bottomframe,width=1600,height=650)
x.pack(side=LEFT,expand=YES,fill=BOTH)
root.title("College management")
root.geometry("1600x800+0+0")
gif1 = PhotoImage(file = 'HMR.gif')
y.create_image(0, 0, image = gif1, anchor = NW)


instruction=Label(x,text='Kindly Fill The Following Fields\n')
instruction.grid(sticky=N)
rollnol = Label(x,text='Roll Number')
namel = Label(x, text='Name') # More labels
emaill = Label(x, text='Email') # ^
rollnol.grid(row=1, sticky=N)
namel.grid(row=2, sticky=N)
emaill.grid(row=3, sticky=N)
rollnoe = Entry(x)
namee = Entry(x) # The entry input
emaile = Entry(x)
rollnoe.grid(row=1,column=1)
namee.grid(row=2, column=1)
emaile.grid(row=3, column=1)
name=namee.get()
rollno=rollnoe.get()
email=emaile.get()
def Modify():
    x.delete("all")
    cur.execute("")

def Addec():
   x.delete("all")
   cur.execute("INSERT INTO ec VALUES('%s','%s','%s')"%(rollno,name,email))
   db.commit()

def Addee():
   x.delete("all")
   cur.execute("INSERT INTO ee VALUES('%s','%s','%s')"%(rollno,name,email))
   db.commit()

def Addcse():
   x.delete("all")
   cur.execute("INSERT INTO cse VALUES('%s','%s','%s')"%(rollno,name,email))
   db.commit()
 
def Delete():
   x.delete("all")
   cur.execute("DELETE FROM ee,ec,cse WHERE roll_no='%s'"%(rollno))
   db.commit()

        



#modifybutton= Button(topframe,text="EDIT",fg="blue",command=Modify)
addcsebutton= Button(topframe,text="ADD TO CSE",fg="blue",command=Addcse)
addeebutton= Button(topframe,text="ADD TO EE",fg="blue",command=Addee)
addecbutton= Button(topframe,text="ADD TO EC",fg="blue",command=Addec)
deletebutton= Button(topframe,text="DELETE",fg="blue",command=Delete)

#modifybutton.configure(relief=FLAT)
addcsebutton.configure(relief=FLAT)
addeebutton.configure(relief=FLAT)
addecbutton.configure(relief=FLAT)
deletebutton.configure(relief=FLAT)

#modifybutton_window = y.create_window(560, 100, anchor=W, window=modifybutton)
addcsebutton_window = y.create_window(500, 100, anchor=W, window=addcsebutton)
addeebutton_window = y.create_window(600, 100, anchor=W, window=addeebutton)
addecbutton_window = y.create_window(700, 100, anchor=W, window=addecbutton)
deletebutton_window = y.create_window(800, 100, anchor=W, window=deletebutton)
m = Menu(root)
root.config(m=m)
filemenu = Menu(m)
m.add_cascade(label="File", m=filemenu)
filemenu.add_command(label="Exit", command=root.destroy)


root.mainloop()
