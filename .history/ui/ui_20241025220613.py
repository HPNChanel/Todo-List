import tkinter as tk
from tkinter import ttk
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
  