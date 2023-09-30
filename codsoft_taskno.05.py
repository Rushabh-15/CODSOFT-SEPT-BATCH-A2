from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")

        self.contacts = []

        # Create a notebook with two tabs
        self.notebook = ttk.Notebook(self.root)
        self.tab1 = Frame(self.notebook,bg="darkturquoise")  # Set background color using 'bg'
        self.tab2 = Frame(self.notebook,bg="darkturquoise")  # Set background color using 'bg'
        self.notebook.add(self.tab1, text="Add Contact")
        self.notebook.add(self.tab2, text="View Contacts")
        self.notebook.pack()

        # Initialize tab 1 (Add Contact)
        self.init_add_contact_tab()

        # Initialize tab 2 (View Contacts)
        self.init_view_contacts_tab()


    def init_add_contact_tab(self):
        label = Label(self.tab1, text="Add Contact", font=("Arial", 20), bg = "#FF9912")
        label.pack(pady=10)

        name_label = Label(self.tab1, text="Name:", font=("Arial", 15), bg = "lawngreen")
        name_label.pack()
        self.name_entry = Entry(self.tab1, font=("Arial", 15))
        self.name_entry.pack()

        phone_label = Label(self.tab1, text="Phone:", font=("Arial", 15), bg = "lawngreen")
        phone_label.pack()
        self.phone_entry = Entry(self.tab1, font=("Arial", 15))
        self.phone_entry.pack()

        email_label = Label(self.tab1, text="Email:", font=("Arial", 15), bg = "lawngreen")
        email_label.pack()
        self.email_entry = Entry(self.tab1, font=("Arial", 15))
        self.email_entry.pack()

        address_label = Label(self.tab1, text="Address:", font=("Arial", 15), bg = "lawngreen")
        address_label.pack()
        self.address_entry = Entry(self.tab1, font=("Arial", 15))
        self.address_entry.pack()

        add_button = Button(self.tab1, text="Add Contact", command=self.add_contact, font=("Arial", 15), bg = "lawngreen")
        add_button.pack(pady=10)

    def init_view_contacts_tab(self):
        label = Label(self.tab2, text="View Contacts", font=("Arial", 20), bg = "#FF9912")
        label.pack(pady=10)

        search_label = Label(self.tab2, text="Search:", font=("Arial", 15), bg = "lawngreen")
        search_label.pack()
        self.search_entry = Entry(self.tab2, font=("Arial", 15))
        self.search_entry.pack()

        search_button = Button(self.tab2, text="Search", command=self.search_contacts, font=("Arial", 15), bg = "lawngreen")
        search_button.pack(pady=5)

        self.contacts_treeview = ttk.Treeview(self.tab2, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.contacts_treeview.heading("Name", text="Name")
        self.contacts_treeview.heading("Phone", text="Phone")
        self.contacts_treeview.heading("Email", text="Email")
        self.contacts_treeview.heading("Address", text="Address")
        self.contacts_treeview.pack(padx=10, pady=10)
        self.update_contacts_treeview()

        edit_button = Button(self.tab2, text="Edit Contact", command=self.edit_contact, font=("Arial", 15), bg = "lawngreen")
        edit_button.pack(pady=5)

        delete_button = Button(self.tab2, text="Delete Contact", command=self.delete_contact, font=("Arial", 15), bg = "lawngreen")
        delete_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            self.clear_add_contact_fields()
            self.update_contacts_treeview()
            showinfo("Success", "Contact added successfully!")
        else:
            showwarning("Error", "Name and Phone are required!")

    def clear_add_contact_fields(self):
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

    def update_contacts_treeview(self):
        self.contacts_treeview.delete(*self.contacts_treeview.get_children())
        for contact in self.contacts:
            self.contacts_treeview.insert("", "end", values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def search_contacts(self):
        search_text = self.search_entry.get().strip().lower()
        found_match = False  # Flag to check if any matches were found

        for item in self.contacts_treeview.get_children():
            values = self.contacts_treeview.item(item, 'values')
            name_match = values[0].lower() == search_text
            phone_match = values[1].lower() == search_text
            if name_match or phone_match:
                self.contacts_treeview.selection_set(item)
                self.contacts_treeview.focus(item)
                found_match = True  # Match found, set the flag to True

        if not found_match:
            showinfo("Info", f"No contact with '{search_text}' found.")

    def edit_contact(self):
        selected_item = self.contacts_treeview.selection()
        if selected_item:
            selected_contact = self.contacts[self.contacts_treeview.index(selected_item)]
            
            # Create a new window for editing
            edit_window = Toplevel(self.root)
            edit_window.title("Edit Contact")
            edit_window.geometry("300x300")
            edit_window.config(bg = "darkturquoise")

            edit_name_label = Label(edit_window, text="Name:", font=("Arial", 15), bg="lawngreen")
            edit_name_label.pack()
            edit_name_entry = Entry(edit_window, font=("Arial", 15))
            edit_name_entry.pack()
            edit_name_entry.insert(0, selected_contact["Name"])

            edit_phone_label = Label(edit_window, text="Phone:", font=("Arial", 15), bg="lawngreen")
            edit_phone_label.pack()
            edit_phone_entry = Entry(edit_window, font=("Arial", 15))
            edit_phone_entry.pack()
            edit_phone_entry.insert(0, selected_contact["Phone"])

            edit_email_label = Label(edit_window, text="Email:", font=("Arial", 15), bg="lawngreen")
            edit_email_label.pack()
            edit_email_entry = Entry(edit_window, font=("Arial", 15))
            edit_email_entry.pack()
            edit_email_entry.insert(0, selected_contact["Email"])

            edit_address_label = Label(edit_window, text="Address:", font=("Arial", 15), bg="lawngreen")
            edit_address_label.pack()
            edit_address_entry = Entry(edit_window, font=("Arial", 15))
            edit_address_entry.pack()
            edit_address_entry.insert(0, selected_contact["Address"])

            def save_edited_contact():
                selected_contact["Name"] = edit_name_entry.get()
                selected_contact["Phone"] = edit_phone_entry.get()
                selected_contact["Email"] = edit_email_entry.get()
                selected_contact["Address"] = edit_address_entry.get()
                self.update_contacts_treeview()
                edit_window.destroy()

            save_button = Button(edit_window, text="Save", command=save_edited_contact, font=("Arial", 15), bg = "lawngreen")
            save_button.pack(pady=10)

    def delete_contact(self):
        selected_item = self.contacts_treeview.selection()
        if selected_item:
            selected_contact = self.contacts[self.contacts_treeview.index(selected_item)]
            self.contacts.remove(selected_contact)
            self.update_contacts_treeview()
            showinfo("Success", "Contact deleted successfully!")

if __name__ == "__main__":
    root = Tk()
    app = ContactBookApp(root)
    root.mainloop()
