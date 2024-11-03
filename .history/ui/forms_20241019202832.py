import tkinter as tk

class TaskForm:
  def __init__(self, root, add_task_callback):
    self.root = root
    self.add_task_callback = add_task_callback
  
  def show(self):
    #* Create PopUp Window to add a new task
    form_window = tk.Toplevel(self.root)  #* Toplevel() is used to create a top-level window, just an independent window that pop 