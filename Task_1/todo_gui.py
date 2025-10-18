import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file if it exists"""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("✅ To-Do List App")
        self.root.geometry("500x600")
        self.root.config(bg="#f8f9fa")

        self.tasks=load_tasks()

        tk.Label(self.root, text="🗂 To-Do List",font=("Helvetica", 20, "bold"),bg="#f8f9fa",fg="#212529").pack(pady=15)

        entry_frame=tk.Frame(self.root,bg="#f8f9fa")
        entry_frame.pack(pady=10)

        self.task_entry=tk.Entry(entry_frame,font=("Arial", 14),width=30,bd=2,relief="groove")
        self.task_entry.grid(row=0,column=0,padx=10,pady=5)

        add_btn=tk.Button(entry_frame,text="Add Task",font=("Arial",12,"bold"),bg="#007bff",fg="white",width=10,command=self.add_task)
        add_btn.grid(row=0,column=1)
        list_frame=tk.Frame(self.root,bg="#f8f9fa")
        list_frame.pack(pady=10)
        self.scrollbar=tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.listbox=tk.Listbox(list_frame,font=("Arial",13),width=45,height=15,bd=2,relief="groove",selectmode=tk.SINGLE,yscrollcommand=self.scrollbar.set,selectbackground="#cfe2ff")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.listbox.yview)
     
        btn_frame=tk.Frame(self.root, bg="#f8f9fa")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame,text="Mark Done",font=("Arial",11,"bold"),bg="#198754",fg="white",width=12,command=self.mark_done).grid(row=0,column=0,padx=5)
        tk.Button(btn_frame,text="Delete Task", font=("Arial",11,"bold"),bg="#dc3545",fg="white",width=12,command=self.delete_task).grid(row=0, column=1,padx=5)
        tk.Button(btn_frame,text="Clear All",font=("Arial",11,"bold"),bg="#fd7e14",fg="white",width=12,command=self.clear_all).grid(row=0,column=2,padx=5)
        tk.Button(btn_frame, text="Exit",font=("Arial",11,"bold"),bg="#6c757d",fg="white",width=12,command=self.root.destroy).grid(row=0, column=3, padx=5)

        self.refresh_listbox()

    def refresh_listbox(self):
        """Refresh the Listbox"""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status="✔" if task["completed"] else "❌"
            self.listbox.insert(tk.END, f"{status}  {task['title']}")

    def add_task(self):
        """Add a new task"""
        title=self.task_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning","Please enter a task!")
            return
        self.tasks.append({"title": title,"completed": False})
        save_tasks(self.tasks)
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def mark_done(self):
        """Mark selected task as complete"""
        try:
            index=self.listbox.curselection()[0]
            self.tasks[index]["completed"]=True
            save_tasks(self.tasks)
            self.refresh_listbox()
        except IndexError:
            messagebox.showinfo("Info", "Select a task to mark as done.")

    def delete_task(self):
        """Delete selected task"""
        try:
            index=self.listbox.curselection()[0]
            deleted=self.tasks.pop(index)
            save_tasks(self.tasks)
            self.refresh_listbox()
            messagebox.showinfo("Deleted", f"Deleted: {deleted['title']}")
        except IndexError:
            messagebox.showinfo("Info", "Select a task to delete.")

    def clear_all(self):
        """Clear all tasks"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            save_tasks(self.tasks)
            self.refresh_listbox()

if __name__=="__main__":
    root=tk.Tk()
    app=ToDoApp(root)
    root.mainloop()
