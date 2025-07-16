import tkinter as tk
from tkinter import messagebox



#creating the main window where the complete system will be displayed
window=tk.Tk()
window.title("Contact Book") #adding the title of the window
window.geometry ("500x600") #defining the size of window

contacts={}

#adding the contact details 
tk.Label (window,text="NAME",font=("Arial",12 ,"bold")).pack()
name=tk.Entry(window,width="40")
name.pack(pady=20)

tk.Label (window,text="PHONE NUMBER",font=("Arial",12,"bold")).pack()
phone_number=tk.Entry(window,width="40")
phone_number.pack(pady=20)

tk.Label (window,text="EMAIL",font=("Arial",12,"bold")).pack()
email=tk.Entry(window,width="40")
email.pack(pady=20)

tk.Label (window,text="ADDRESS",font=("Arial",12,"bold")).pack()
address=tk.Entry(window,width="40")
address.pack(pady=20)

#saving the details of the contact
def save_contact():
    name_entered=name.get()
    phone_number_entered= phone_number.get()
    email_entered= email.get()
    address_entered=address.get()
    
    if name_entered and phone_number_entered:
        contacts[name] = {"Phone": phone_number_entered, "Email": email_entered, "Address": address_entered}
        messagebox.showinfo("Contact Saved")
    else:
        messagebox.showwarning("Please Enter the NAME and PHONE NUMBER")



tk.Button(window,text="Save contact",bg="Green",font=("Arial",8,"bold"),command=save_contact).pack(pady=10)
































window.mainloop()