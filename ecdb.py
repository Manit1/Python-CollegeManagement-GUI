from Tkinter import *
import ttk
import MySQLdb
root = Tk()
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="college")        # name of the data base
   
y=Canvas(root,width=1600,height=1500,background="#2E86C1")
y.pack(side=LEFT,expand=YES,fill=BOTH)
text=Text(y,height=1000,width=1000)
text.pack()
cursor = db.cursor()
cursor.execute("SELECT * FROM ec")
rows=cursor.fetchall()
for x in rows:
  text.insert(END,"\n"+str(tuple(x)))
db.close()
root.mainloop()
