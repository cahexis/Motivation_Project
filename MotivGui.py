import tkinter as tk




#Main window
root = tk.Tk()
root.title("Motivation :D")
root.geometry('400x400')

root.resizable(width=False, height=False)

# Buttons
remove = tk.Button(root, text="-", font=('Verdana', 30),foreground='red')
remove.place(x=30,y=75)

add = tk.Button(root, text="+", font=('Verdana', 30),foreground='green')
add.place(x=300,y=75)

root.mainloop()