from tkinter import ttk, Toplevel, messagebox
from datetime import datetime
import tkinter as tk 

class TaskTable(ttk.Frame):
    def __init__(self, parent, task_manager):
        super().__init__(parent)
        self.task_manager = task_manager
        self.columns = ("ID", "Task", "Priority", "Due Date", "Status")

        # Set up Treeview for the task table
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings", height=10)
        self.tree.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.update_table()
        
        self.tree.tag_configure("red", background="#f28b82")
        self.tree.tag_configure("orange", background="#fdd835")
        self.tree.tag_configure("green", background="#ccff90")

        # Frame containing the action buttons
        button_frame = tk.Frame(self, bg="#f0f0f0")
        button_frame.pack(side="right", fill="y", padx=5)

        self.edit_button = ttk.Button(button_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=(0, 10))

        self.complete_button = ttk.Button(button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=(0, 10))

        self.delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=(0, 10))

    def update_table(self):
        # Clear old data and reload new data into the table
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        tasks = self.task_manager.get_all_tasks()
        for task in tasks:
            priority = task[2]
            color = "green" if priority == "Low" else "orange" if 
            self.tree.insert("", "end", values=task, tags=(color,))

        # Configure row colors based on priority
        self.tree.tag_configure("red", background="#f28b82")
        self.tree.tag_configure("orange", background="#fdd835")
        self.tree.tag_configure("green", background="#ccff90")

    def complete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item[0])['values'][0]
            completed_date = datetime.now().strftime('%Y-%m-%d')
            self.task_manager.complete_task(task_id)
            self.update_table()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
      
    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item[0])['values'][0]
            self.task_manager.delete_task(task_id)
            self.update_table()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
    def edit_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            task_id = self.tree.item(selected_item[0])['values'][0]
            task = self.tree.item(selected_item[0])['values'][1]
            priority = self.tree.item(selected_item[0])['values'][2]
            due_date = self.tree.item(selected_item[0])['values'][3]
            
            # Open edit window
            edit_window = Toplevel(self)
            edit_window.title("Edit Task")
            edit_window.geometry("400x200")

            ttk.Label(edit_window, text="Task:").grid(row=0, column=0, pady=5, padx=5)
            task_entry = ttk.Entry(edit_window, width=40)
            task_entry.grid(row=0, column=1, pady=5, padx=5)
            task_entry.insert(0, task)

            ttk.Label(edit_window, text="Priority:").grid(row=1, column=0, pady=5, padx=5)
            priority_var = tk.StringVar(value=priority)
            priority_options = ['Low', 'Medium', 'High']
            priority_menu = ttk.Combobox(edit_window, textvariable=priority_var, values=priority_options, width=38)
            priority_menu.grid(row=1, column=1, pady=5, padx=5)

            ttk.Label(edit_window, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, pady=5, padx=5)
            due_date_entry = ttk.Entry(edit_window, width=40)
            due_date_entry.grid(row=2, column=1, pady=5, padx=5)
            due_date_entry.insert(0, due_date)

            def save_changes():
                new_task = task_entry.get()
                new_priority = priority_var.get()
                new_due_date = due_date_entry.get()

                if new_task and new_priority and new_due_date:
                    self.task_manager.edit_task(task_id, new_task, new_priority, new_due_date)
                    self.update_table()
                    edit_window.destroy()
                else:
                    messagebox.showwarning("Input Error", "Please fill all fields.")

            save_button = ttk.Button(edit_window, text="Save Changes", command=save_changes)
            save_button.grid(row=3, column=1, pady=10)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")
