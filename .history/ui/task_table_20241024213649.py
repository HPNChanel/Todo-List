import tkinter as tk
from tkinter import ttk
from ..task.task_manager import get_all_tasks, complete_task, delete_task, update_task

class TaskTable(tk.Frame):
  def __init__(self):