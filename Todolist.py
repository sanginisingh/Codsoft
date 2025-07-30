import tkinter as tk

window=tk.Tk()
window.title("TO-DO LIST")
window.geometry("500x500")

tk.Label (window,text="ADD TO THE LIST",font=("Arial",10,"bold")).pack()
addTask=tk.Entry(window,width=40)
addTask.pack(pady=10)

def add_task():
    task=addTask.get()
    if task:
        todoList.insert(tk.END,task)
        addTask.delete(0,tk.END)
tk.Button(window,text="ADD",command=add_task, width= 10,bg="light green").pack(pady=5)
    
    
tk.Label(window,text="DELETE FROM THE LIST",font=("Arial", 10, "bold")).pack()
deleteTask= tk.Entry(window,width=40)
deleteTask.pack(pady=10)

def delete_task():
    taskDelete= deleteTask.get()
    found= False
    for i in range(todoList.size()):
        if todoList.get(i)==taskDelete:
            todoList.delete(i)
            deleteTask.delete(0,tk.END)
            found =True
            break
tk.Button(window,text="DELETE",width=10,bg="yellow",command=delete_task).pack(pady=5)


tk.Label(window,text="TO-DO LIST",font=("Arial",10,"bold")).pack()
view_frame=tk.Frame(window)
view_frame.pack(pady=10)
todoList= tk.Listbox(view_frame,width=50,height=10,selectmode=tk.EXTENDED)
todoList.pack()

def mark_as_done():
    selected_items = list(todoList.curselection())
    for i in selected_items:
        task = todoList.get(i)
        if not task.endswith("✔️"):
            todoList.delete(i)
            todoList.insert(i, task + " ✔️")

clear_frame=tk.Frame(window)
clear_frame.pack(pady=10)

def clearAll():
    todoList.delete(0,tk.END)

tk.Button(window, text="Mark as Done", command=mark_as_done, bg="lightblue", width=15).pack(padx=5)

tk.Button(window, text="Clear All", command=clearAll, bg="red", fg="white", width=15).pack(padx=5)



window.mainloop()






