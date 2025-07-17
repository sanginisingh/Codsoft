import tkinter as tk
from tkinter import messagebox



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

#saving the details of the contact
def save_contact():
    name_entered=name.get()
    phone_number_entered= phone_number.get()
    email_entered= email.get()
    address_entered=address.get()
    
    if name_entered and phone_number_entered:
        contacts[name] = {"Phone": phone_number_entered, "Email": email_entered, "Address": address_entered}
        messagebox.showinfo("Success","Contact Saved")
        clear()
    else:
        messagebox.showwarning("Please Enter the NAME and PHONE NUMBER")
      
tk.Button(window,text="Save contact",bg="Green",font=("Arial",8,"bold"),command=save_contact).pack(pady=10)



result_box = tk.Text(window, height=10, width=30)
result_box.pack(pady=10)
def view_contact():
    result_box.delete(1.0, tk.END)  
    

    if not contacts:
        result_box.insert(tk.END, "No contacts available.\n")
        return
    for name, info in contacts.items():
        result_box.insert(tk.END, f"Name: {name}\n")
        result_box.insert(tk.END, f"Phone: {info['Phone']}\n")
        result_box.insert(tk.END, f"Email: {info['Email']}\n")
        result_box.insert(tk.END, f"Address: {info['Address']}\n")
        result_box.insert(tk.END, "-"*40 + "\n")
    clear()
    
tk.Button(window,text="View contact list",bg="Yellow",font=("Arial",8,"bold"),command=view_contact).pack(pady=10)


def clear():
    name.delete(0,tk.END)
    phone_number.delete(0,tk.END)
    email.delete(0,tk.END)
    address.delete(0,tk.END)

# adding the search feature

search_frame = tk.Frame(window)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
search = tk.Entry(search_frame, width=20)
search.pack(side="left", padx=5)

def search_contact():
    query = search.get().lower()
    result_box.delete(1.0, tk.END)

    found = False
    for contact_name in contacts:
        if query in contact_name.lower():
            result_box.insert(tk.END, contact_name + "\n")
            found = True

    if not found:
        result_box.insert(tk.END, "No matching contacts found.\n")

tk.Button(search_frame, text="Search", command=search).pack(side="left", padx=5)

update_frame = tk.Frame(window)
update_frame.pack(pady=10)

tk.Label(update_frame, text="Update:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
update = tk.Entry(update_frame, width=20)
update.pack(side="left", padx=5)
tk.Button(update_frame, text="Update", command=update).pack(side="left", padx=5)

delete_frame = tk.Frame(window)
delete_frame.pack(pady=10)

tk.Label(delete_frame, text="Delete:", font=("Arial", 10, "bold")).pack(side="left", padx=5)
delete = tk.Entry(delete_frame, width=20)
delete.pack(side="left", padx=5)
tk.Button(delete_frame, text="Delete", command=delete).pack(side="left", padx=5)


































window.mainloop()