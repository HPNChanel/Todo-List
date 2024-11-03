import tkinter as tk
from tkinter import ttk
from datetime import datetime
from task.task_manager import get_all_tasks, complete_task, delete_task, update_task

class TaskTable(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent, bg="#f0f0f0")
    self.columns = ("ID", "Task", "Priority", "Due Date", "Status")
    
    self.tree = ttk.Treeview(self, columns=self.columns, show="headings", height=10)
    self.tree.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 10))
    
    for col in self.columns:
      self.tree.heading(col, text=col)
      self.tree.column(col, anchor="center")
    
    self.update_table()

    #* Add Edit, Delete Button for each task line
    button_frame = tk.Frame(self, bg="#f0f0f0")
    button_frame.pack(side=tk.RIGHT, fill="y", padx=5)
    
    self.edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=15, bg="#FFC107", fg="#fff")
    self.edit_button.pack(pady=(0, 10), padx=10)
    
    self.complete_button = tk.Button(button_frame, text="Complete Task", command=self.complete_task, width=15, bg="#2196F3", fg="#fff")
    self.complete_button.pack(pady=(0, 10), padx=10)
    
    self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_task,  width=15, bg="#F44336", fg="white")
    self.delete_button.pack(pady=(0, 10), padx=10)
    
  
  def update_table(self):
    for row in self.tree.get_children():
      self.tree.delete(row)
    
    tasks = get_all_tasks()
    for task in tasks:
      self.tree.insert("", "end", values=task)
  
  def delete_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      delete_task(task_id)
      self.update_table()
    else:
      tk.messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
  def complete_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      completed_date = datetime.now().strftime('%Y-%m-%d')
      complete_task(task_id, completed_date)
      self.update_table()
    else:
      tk.messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

  def edit_task(self):
    selected_item = self.tree.selection()
    if selected_item:
      task_id = self.tree.item(selected_item[0])['values'][0]
      task = self.tree.item(selected_item[0])['values'][1]
      priority = self.tree.item(selected_item[0])['values'][2]
      due_date = self.tree.item(selected_item[0])['values'][3]
      
      edit_window = tk.Toplevel(self)
      edit_window.title("Edit Task")
      
      tk.Label(edit_window, text="Task:").grid(row=0, column=0)
      task_entry = tk.Entry(edit_window, width=40) #NOTE
      task_entry.grid(row=0, column=1)
      task_entry.insert(0, task)
      
      tk.Label(edit_window, text="Priority:").grid(row=1, column=0)
      priority_var = tk.StringVar(value=priority)  #NOTE
      priority_options = ['Low', 'Medium', 'High']
      priority_menu = ttk.Combobox(edit_window, textvariable=priority_var, values=priority_options, width=38)
      priority_menu.grid(row=1, column=1)
      
      tk.Label(edit_window)