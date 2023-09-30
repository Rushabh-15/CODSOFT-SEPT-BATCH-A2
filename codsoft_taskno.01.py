from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("To-Do List App")
root.geometry("830x730+325+50")
root.config(bg = "darkturquoise")
f = ("Arial", 20, "bold")

lab_header = Label(root, text = "To-Do list", font= f)
lab_header.pack(pady=20)

lab_name = Label(root, text = "Plan for today: ", font = f)
lab_name.pack()

listbox = Listbox(root, font=f, width=30)
listbox.pack(pady=10)

lab_entry = Label(root, text = "From here you can add your task: ", font = f)
lab_entry.pack()
ent_entry = Entry(root, font = f, width = 20)
ent_entry.pack(pady=10)

def add_task():
	task = ent_entry.get()
	if task.strip():
		listbox.insert(END, task)
		ent_entry.delete(0, END)
	else:
		showerror("Warning", "Please enter some task.")
		ent_entry.focus_set()

def remove_task():
	selected_task = listbox.curselection()
	if selected_task:
		listbox.delete(selected_task)
		showinfo("Success", "Task has been removed successfully!! ")

btn_add = Button(root, text="Add Task", command=add_task, font = f, bg = "lawngreen")
btn_add.pack(pady=10)
 
btn_remove = Button(root, text="Remove Task", command=remove_task, font = f, bg = "firebrick1")
btn_remove.pack(pady=10)

root.mainloop()
