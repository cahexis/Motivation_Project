import tkinter as tk
import sqlite3

#reference db from other file
connect = sqlite3.connect("applied.db")
cursor = connect.cursor()


def getcurrentval():
    cursor.execute("SELECT jobs FROM Applied_Jobs")
    row = cursor.fetchone()
    return row[0] if row else 0

def updateval():
    current_val = getcurrentval()
    print(current_val)



#functions for adding/subtracting to the db value
def addval():
    cursor.execute("UPDATE Applied_Jobs SET jobs = jobs + 1")
    connect.commit()
    updateval()

    
    

def subval():
    cursor.execute("UPDATE Applied_Jobs SET jobs = jobs - 1")
    connect.commit()
    updateval()
      

#Main window
root = tk.Tk()
root.title("Motivation :D")
root.geometry('400x400')
root.resizable(width=False, height=False)

# Buttons
remove = tk.Button(root, text="-", font=('Verdana', 30),foreground='red', command=subval)
remove.place(x=30,y=75)

add = tk.Button(root, text="+", font=('Verdana', 30),foreground='green', command=addval)
add.place(x=300,y=75)

updateval()

root.mainloop()