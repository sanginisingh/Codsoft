import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



#creating the main window where the complete system will be displayed
window=tk.Tk()
window.title("Contact Book") #adding the title of the window
window.geometry ("500x700") #defining the size of window

contacts={}

#adding the contact details 
tk.Label (window,text="NAME",font=("Arial",12 ,"bold")).pack() 
name=tk.Entry(window,width="40")
name.pack(pady=10)

tk.Label (window,text="PHONE NUMBER",font=("Arial",12,"bold")).pack()
phone_number=tk.Entry(window,width="40")
phone_number.pack(pady=10)

tk.Label (window,text="EMAIL",font=("Arial",12,"bold")).pack()
email=tk.Entry(window,width="40")
email.pack(pady=10)

tk.Label (window,text="ADDRESS",font=("Arial",12,"bold")).pack()
address=tk.Entry(window,width="40")
address.pack(pady=10)

def clear():
    name.delete(0,tk.END)
    phone_number.delete(0,tk.END)
    email.delete(0,tk.END)
    address.delete(0,tk.END)

#saving the details of the contact
def save_contact():
    name_entered=name.get()
    phone_number_entered= phone_number.get()
    email_entered= email.get()
    address_entered=address.get()
    
    if name_entered and phone_number_entered:
        contacts[name_entered] = {
    "Phone": phone_number_entered,
    "Email": email_entered,
    "Address": address_entered}
        messagebox.showinfo("Success","Contact Saved")
        refresh_contact_list()
        clear()
    else:
        messagebox.showwarning("Please Enter the NAME and PHONE NUMBER")

tk.Button(window,text="Save contact",bg="Green",font=("Arial",8,"bold"),command=save_contact).pack(pady=10)
    
      


# adding the search feature

search_frame = tk.Frame(window)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
search = tk.Entry(search_frame, width=20)
search.pack(side="left", padx=5)

search_dropdown = ttk.Combobox(search_frame, width=20, state="readonly")
search_dropdown.pack(side="left", padx=5)
search_dropdown.set("Select Contact")

def show_selected_contact(event):
    name = search_dropdown.get()
    contact = contacts.get(name)
    if contact:
        messagebox.showinfo("Contact Details",
                            f"Name: {name}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")

search_dropdown.bind("<<ComboboxSelected>>", show_selected_contact)

def search_contact():
    search_term = search.get().strip().lower()
    matches = [name for name in contacts if search_term in name.lower()]

    if matches:
        search_dropdown["values"] = matches
        search_dropdown.set("Select Contact")
    else:
        search_dropdown["values"] = []
        search_dropdown.set("No match found")
        messagebox.showinfo("Not Found", "No contact matched your search.")
    search_dropdown.event_generate('<Button-1>')

tk.Button(search_frame, text="Search", command=search_contact).pack(side="left", padx=5)

#adding the delete feature
delete_frame = tk.Frame(window)
delete_frame.pack(pady=10)

tk.Label(delete_frame, text="Delete:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
delete = tk.Entry(delete_frame, width=20)
delete.pack(side="left", padx=5)

def delete_contact():
    name = delete.get().strip()
    if name in contacts:
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete contact: {name}?")
        if confirm:
            del contacts[name]
            messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully.")
            refresh_contact_list()
            clear()
    else:
        messagebox.showwarning("Not Found", f"No contact found with the name: {name}")

tk.Button(delete_frame, text="Delete", command=delete_contact).pack(side="left", padx=5)


view_frame = tk.Frame(window)
view_frame.pack(pady=20)

tk.Label(view_frame, text="All Contacts", font=("Arial", 12, "bold")).pack()

# Scrollbar and Listbox
scrollbar = tk.Scrollbar(view_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_listbox = tk.Listbox(view_frame, width=50, height=10, yscrollcommand=scrollbar.set)
contact_listbox.pack()

scrollbar.config(command=contact_listbox.yview)



def refresh_contact_list():
    contact_listbox.delete(0, tk.END)  # Clear current items
    for name in contacts:
        contact_listbox.insert(tk.END, name)


def show_contact_details(event):
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0])
        contact = contacts.get(name)
        if contact:
            messagebox.showinfo("Contact Details",
                                f"Name: {name}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")

contact_listbox.bind("<<ListboxSelect>>", show_contact_details)








































window.mainloop()