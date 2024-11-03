import tkinter as tk
from tkinter import ttk
from ..task.task_manager import get_all_tasks, complete_task, delete_task, update_task

class TaskTable(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    self.columns = ("ID", "Task", "Priority", "Due Date", "Status")
    
    self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
    self.tree.pack(side=tk.LEFT)
    
    for col in self.columns:
      self.tree.heading(col, text=col)
    
    self.update_table()

    #* Add Edit, Delete Button for each task line
    button_frame = tk.Frame(self)
    button_frame.pack(side=tk.RIGHT)
    
    self.edit_button = tk.Button(button_frame, text="Edit", command=self.edit_task)
    self.edit_button.pack()
    
    self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_task)
    self.delete_button.pack()
    
    self.complete_button = tk.Button(button_frame, text="Complete", command=self.complete_task)
    self.complete_button.pack()
  
  def update_table()
    