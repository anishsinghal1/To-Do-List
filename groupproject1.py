import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # create the widgets
        self.label_task = tk.Label(self.master, text="Task:")
        self.entry_task = tk.Entry(self.master)
        self.label_desc = tk.Label(self.master, text="Description:")
        self.entry_desc = tk.Entry(self.master)
        self.label_due = tk.Label(self.master, text="Due date (YYYY-MM-DD):")
        self.entry_due = tk.Entry(self.master)
        self.btn_add = tk.Button(self.master, text="Add task", command=self.add_task)
        self.btn_display = tk.Button(self.master, text="Display tasks", command=self.display_tasks)

        # grid the widgets
        self.label_task.grid(row=0, column=0, sticky="w")
        self.entry_task.grid(row=0, column=1)
        self.label_desc.grid(row=1, column=0, sticky="w")
        self.entry_desc.grid(row=1, column=1)
        self.label_due.grid(row=2, column=0, sticky="w")
        self.entry_due.grid(row=2, column=1)
        self.btn_add.grid(row=3, column=0)
        self.btn_display.grid(row=3, column=1)

    def add_task(self):
        task_name = self.entry_task.get()
        task_desc = self.entry_desc.get()
        task_due_str = self.entry_due.get()

        # validate due date input
        try:
            task_due = datetime.strptime(task_due_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid due date format. Please use YYYY-MM-DD.")
            return

        # save task to file
        with open("todo.txt", "a") as f:
            f.write(f"{task_name},{task_desc},{task_due_str}\n")

        # clear input fields
        self.entry_task.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.entry_due.delete(0, tk.END)

        messagebox.showinfo("Success", "Task added successfully!")

    def display_tasks(self):
        try:
            # read tasks from file
            with open("todo.txt", "r") as f:
                tasks = [line.strip().split(",") for line in f.readlines()]
        except FileNotFoundError:
            messagebox.showinfo("No tasks", "There are currently no tasks.")
            return

        # sort tasks by due date
        tasks_sorted = sorted(tasks, key=lambda x: datetime.strptime(x[2], "%Y-%m-%d"))

        # create and display task list
        task_list = "\n".join([f"{i + 1}. {task[0]} - {task[1]} - {task[2]}" for i, task in enumerate(tasks_sorted)])
        messagebox.showinfo("Tasks", task_list)


root = tk.Tk()
app = ToDoList(root)
root.mainloop()
