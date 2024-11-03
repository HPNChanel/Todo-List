import tkinter as tk
from tkinter import ttk
from ui import task_table
from ui.task_table import TaskTable
from task.task_manager import add_new_task, get_all_tasks

def create_ui():
  root = tk.Tk()  #* Tk(): constructor method used to create the main application window
  root.title("Todo List")
  root.geometry("600x450")
  root.configure(bg="#f0f0f0")  #* Configure background for app
  
  #* Frame for task input form
  form_frame = tk.LabelFrame(root, text="Add New Task", padx=10, pady=10, bg="#f0f0f0")
  form_frame.pack(padx=15, pady=15, fill="x")
  
  tk.Label(form_frame, text="Task:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
  task_entry = tk.Entry(form_frame, width=40)
  task_entry.grid(row=0, column=1, padx=5, pady=5)
  
  tk.Label(form_frame, text="Priority:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
  priority_options = ["Low", "Medium", "High"]
  priority_var = tk.StringVar(value=priority_options[0])
  priority_menu = ttk.Combobox(form_frame, textvariable=priority_var, values=priority_options, width=38)
  priority_menu.grid(row=1, column=1, padx=5, pady=5)
  
  tk.Label(form_frame, text="Due Date (YYYY-MM-DD):", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
  due_date_entry = tk.Entry(form_frame, width=40)
  due_date_entry.grid(row=2, column=1, padx=5, pady=5)

  #* Add Task Button
  def add_task_ui():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    
    if task and priority and due_date:
      add_new_task(task, priority, due_date)
      task_table.update_table()
      