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
      self.tree.heading(col, text=cold)