import tkinter as tk
from tkinter import messagebox
from task.task_manager import add_new_task, get_all_tasks, complete_task
from ui.forms import TaskForm

def create_ui():
  root = tk.Tk()  #* Tk(): constructor method used to create the main application window
  root.title("Todo List")
  
  
  #* Frame for display task list
  task_listbox = tk.Listbox(root, height=10, )