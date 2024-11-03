import tkinter as tk
from tkinter import ttk
from ui.task_table import TaskTable
from task.task_manager import add_new_task, get_all_tasks

def create_ui():
  root = tk.Tk()  #* Tk(): constructor method used to create the main application window
  root.title("Todo List")
  root.geometry()