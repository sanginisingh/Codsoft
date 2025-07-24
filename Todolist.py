import tkinter as tk

window=tk.Tk()
window.title("TO-DO LIST")
window.geometry("500x500")

tk.Label (window,text="ADD TO THE LIST",font=("Arial",10,"bold")).pack()
addTask=tk.Entry(window,width=40)
addTask.pack(pady=20)

tk.Label(window,text="DELETE FROM THE LIST",font=("Arial", 10, "bold")).pack()
deleteTask= tk.Entry(window,width=40)
deleteTask.pack(pady=20)

tk.Label(window,text="TO-DO LIST",font=("Arial",10,"bold")).pack()

view_frame=tk.Frame(window)
view_frame.pack(pady=20)
todoList= tk.Listbox(view_frame,width=50,height=10)
todoList.pack()












window.mainloop()





