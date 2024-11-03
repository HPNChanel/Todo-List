from tkinter import ttk, Toplevel, messagebox
from datetime import datetime
import tkinter as tk  # Thêm import tkinter để dùng tk.Frame cho button_frame

class TaskTable(ttk.Frame):
  def __init__(self, parent, task_manager):
    super().__init__(parent)
    self.task_manager = task_manager
    self.columns = ("ID", "Task", "Priority", "Due Date", "Status")
    
    self.configure(bg="#f0f0f0")
    
    self.tree = ttk.Treeview(self, columns=self.columns, show="headings", height=10)
    self.tree.pack(side="left", fill="both", expand=True, padx=(0, 10))
    for col in self.columns:
      self.tree.heading(col, text=col)
      self.tree.column(col, anchor="center")
    
    self.update_table()

    #* Add Edit, Delete Button for each task line
    button_frame = tk.Frame(self, bg="#f0f0f0")
    button_frame.pack(side="right", fill="y", padx=5)
    
    self.edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=15, bg="#FFC107", fg="#fff")
    self.edit_button.pack(pady=(0, 10), padx=10)
    
    self.complete_button = tk.Button(button_frame, text="Complete Task", command=self.complete_task, width=15, bg="#2196F3", fg="#fff")
    self.complete_button.pack(pady=(0, 10), padx=10)
    
    self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_task,  width=15, bg="#F44336", fg="white")
    self.delete_button.pack(pady=(0, 10), padx=10)
    
  
  def update_table(self):
    for row in self.tree.get_children():
      self.tree.delete(row)
    tasks = self.task_manager.get_all_tasks()
    for task in tasks:
      self.tree.insert("", "end", values=task)
  
  def complete_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      completed_date = 
      self.task_manager.complete_task(task_id)
      self.update_table()
    else:
      ttk.messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
      
  def delete_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      self.task_manager.delete_task(task_id)
      self.update_table()
    else:
      ttk.messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
  def edit_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      task = self.tree.item(selected_item[0])['values'][1]
      priority = self.tree.item(selected_item[0])['values'][2]
      due_date = self.tree.item(selected_item[0])['values'][3]
      
      edit_window = Toplevel(self)
      edit_window.title("Edit Task")
      edit_window.geometry("400x200")
      
      ttk.Label(edit_window, text="Task:").grid(row=0, column=0, padx=5, pady=5)
      task_entry = ttk.Entry(edit_window, width=40) #NOTE
      task_entry.grid(row=0, column=1, padx=5, pady=5)
      task_entry.insert(0, task)
      
      ttk.Label(edit_window, text="Priority:").grid(row=1, column=0, padx=5, pady=5)
      priority_var = ttk.StringVar(value=priority)  #NOTE
      priority_options = ['Low', 'Medium', 'High']
      priority_menu = ttk.Combobox(edit_window, textvariable=priority_var, values=priority_options, width=38)
      priority_menu.grid(row=1, column=1, padx=5, pady=5)
      
      ttk.Label(edit_window, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
      due_date_entry = ttk.Entry(edit_window, width=40)
      due_date_entry.grid(row=2, column=1, padx=5, pady=5)
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
          ttk.messagebox.showwarning("Input Error", "Please fill all fields.")
      
      save_button = ttk.Button(edit_window, text="Save Changes", command=save_changes, bg="#4CAF50", fg="#fff")
      save_button.grid(row=3, column=1, pady=10)
    
    else:
      ttk.messagebox.showwarning("Selection Error", "Please select a task to edit.")