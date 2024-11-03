import tkinter as tk
from tkinter import ttk
from datetime import datetime
from ui.task_table import TaskTable
from task.task_manager import TaskManager

class TaskAppUI:
  def __init__(self, root, task_manager):
    self.root = root
    self.task_manager = task_manager
    
    self.root.title("Todo List Application")
    self.root.geometry("1255x450")
    self.root.configure(bg="#f0f0f0")
    
    self.create_form()
    self.create_task_table()

  def create_form(self):
    #* Frame for task input form
    form_frame = tk.LabelFrame(self.root, text="Add New Task", padx=10, pady=10, bg="#f0f0f0")
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

    add_button = tk.Button(form_frame, text="Add Task", command=self.add_task_ui, width=20, bg="#4CAF50", fg="white")
    add_button.grid(row=3, column=1, pady=10)
    
  def add_task()