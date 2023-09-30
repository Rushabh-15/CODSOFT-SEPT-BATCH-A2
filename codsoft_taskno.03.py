from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.title("Password Generator App")
root.geometry("650x500+250+100")
root.config(bg="darkturquoise")
f = ("Arial", 20, "bold")

def generate_password():
	password_length = int(length_entry.get())
	if password_length < 2:
		password_label.config(text="Password length must be at least 2 characters")
		return

	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for _ in range(password_length))
	password_label.config(text="Generated Password: " + password)
	copy_button.config(state="normal")

lab_header = Label(root, text = "Random Password generator ", font=f)
lab_header.pack(pady=30)

length_label = Label(root, text="Enter Password Length:", font=f)
length_label.pack()
length_entry = Entry(root, font = f)
length_entry.pack(pady=20)

generate_button = Button(root, text="Generate Password", font=f, command=generate_password, bg = "lawngreen")
generate_button.pack()

password_label = Label(root, text="", font=f)
password_label.pack(pady=20)

def copy_to_clipboard():
	generated_password = password_label.cget("text")[20:]
	pyperclip.copy(generated_password)

copy_button = Button(root, text="Copy Password", font=f, command=copy_to_clipboard, bg="lawngreen", state="disabled")
copy_button.pack(pady=20)

root.mainloop()