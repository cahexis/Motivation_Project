import tkinter as tk




#Main window
root = tk.Tk()
root.title("Motivation :D")
root.geometry('400x400')
root.resizable(width=False, height=False)

# Buttons
remove = tk.Button(root, text="-")
remove.place(x=100,y=100)

add = tk.Button(root, text="+")
add.place(x=200,y=100)

root.mainloop()