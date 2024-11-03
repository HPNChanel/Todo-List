import tkinter as tk

class TaskForm:
  def __init__(self, root, add_task_callback):
    self.root = root
    self.add_task_callback = add_task_callback
  
  def show(self):
    #* Create PopUp Window to add a new task
    form_window = tk.Toplevel(self.root)  #* Toplevel() is used to create a top-level window, just an independent window that pops up separately from the main application 
    form_window.title("Add New Task")  #* This is the title of the window
    
    task_label = tk.Label(form_window, text="Task:")  #* Just like label in HTML
    task_label.pack()
    self.task_entry = tk.Entry(form_window)
    self.task_entry.pack()  #* Organizes widgets in blocks before placing them in the parent widget
    
    priority_label = tk.Label(form_window, text="Priority (Low, Medium, High):")
    priority_label.pack()
    self.priority_entry() = tk.Entry(form_window)
    self.priority_entry().pack()
    
    due_date_label = tk.Label(form_window, text="Due")
    
    