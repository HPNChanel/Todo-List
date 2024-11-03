import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from ui.task_table import TaskTable
from task.task_manager import TaskManager
from utils.utils import validate_data

class TaskAppUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        
        self.root.title("Todo List Application")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")
        
        self.create_form()
        self.create_task_table()
        self.create_action_button()

    def create_form(self):
        # Frame for adding a new task
        form_frame = tk.LabelFrame(self.root, text="Add New Task", padx=10, pady=10, bg="#f0f0f0")
        form_frame.pack(padx=15, pady=15, fill="x")

        tk.Label(form_frame, text="Task:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
        self.task_entry = tk.Entry(form_frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Priority:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
        priority_options = ["Low", "Medium", "High"]
        self.priority_var = tk.StringVar(value=priority_options[0])
        self.priority_menu = ttk.Combobox(form_frame, textvariable=self.priority_var, values=priority_options, width=38)
        self.priority_menu.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Due Date (YYYY-MM-DD):", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
        self.due_date_entry = tk.Entry(form_frame, width=40)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(form_frame, text="Add Task", command=self.add_task, width=20, bg="#4CAF50", fg="white")
        add_button.grid(row=3, column=1, pady=10)

    def create_task_table(self):
        # Frame for displaying tasks
        task_frame = tk.Frame(self.root, bg="#f0f0f0")
        task_frame.pack(pady=10, padx=15, fill="both", expand=True)
        
        # Initialize task display table
        self.task_table = TaskTable(task_frame, self.task_manager)
        self.task_table.pack(fill="both", expand=True)
    
    def create_action_button(self):
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill="x", padx=15, pady=10)
        
        self.edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=15, bg="#FFA726", fg="white")
        self.edit_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.complete_task = tk.Button(button_frame, text="Complete Task", command=self.complete_task, width=15, bg="#66BB6A", fg="white")
        self.complete_task.grid(row=0, column=1, padx=5, pady=5)
        
        self.delete_task = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=15, bg="#EF5350", fg="white")
        self.delete_task.grid(row=0, column=2, padx=5, pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()
        
        # Validate date format before adding task
        if task and priority and validate_data(due_date):
            self.task_manager.add_task(task, priority, due_date)
            self.task_table.update_table()  # Refresh display table
            self.task_entry.delete(0, tk.END)
            self.priority_var.set("Low")
            self.due_date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields with valid data.")
    
    def edit_task(self):
        selected_task = self.task_table.tree.selection()
        if selected_task:
            task_id = self.task_table.tree.item(selected_task[0])['values'][0]
            task_name = self.task_table.tree.item(selected_task[0])['values'][1]
            priority = self.task_table.tree.item(selected_task[0])['values'][2]
            due_date = self.task_table.tree.item(selected_task[0])['values'][3]
            
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Task")
            edit_window.geometry("400x300")
            
            tk.Label(edit_window, text="Task:").grid(row=0, column=0, padx=10, pady=5)
            task_entry = tk.Entry(edit_window, width=30)
            task_entry.grid(row=0, column=1, padx=10, pady=5)
            task_entry.insert(0, task_name)
            
            tk.Label(edit_window, text="Priority:").grid(row=1, column=0, padx=10, pady=5)
            priority_var = tk.StringVar(value=priority)
            priority_options = ["Low", "Medium", "High"]
            priority_menu = ttk.Button(edit_window, textvariable=priority_var, values=priority_options)
            priority_menu.grid(row=1, column=1, padx=10, pady=5)
            
            tk.Label(edit_window, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
            due_date_entry = tk.Entry(edit_window, width=30)
            due_date_entry.grid(row=2, column=1, padx=10, pady=5)
            due_date_entry.insert(0, due_date)
            
            def save_changes():
                new_task_name = task_entry.get()
                new_priority = priority_var.get()
                new_due_date = due_date_entry.get()
                
                if new_task_name and new_priority and validate_data(new_due_date):
                    self.task_manager.edit_task(task_id, new_task_name, new_priority, new_due_date)
                    self.task_table.update_table()
                    edit_window.destroy()
                else:
                    messagebox.showwarning("Input Error", "Please fill all fields correctly.")

            save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
            save_button.grid(row=3, column=1, pady=10)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")
    
    def complete_task(self):
        selected_task = self.task_table.tree.selection()
        if selected_task:
            task_id = self.task_table.tree.item(selected_task[0])['values'][0]
            self.task_manager.complete_task(task_id)
            self.task_table.update_table()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")
    
    def delete_task(self):
        selected_task = self.task_table.tree.selection()
        if selected_task:
            task_id = self.task_table.tree.item(selected_task[0])['values'][0]
            confirm = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this task?")
            if confirm:
                self.task_manager.delete_task(task_id)
                
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    