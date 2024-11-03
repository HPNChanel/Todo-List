import tkinter as tk

class TaskForm:
  def __init__(self, root, submit_callback, task_id=None, task=None, priority=None, due_date=None):
    self.root = root
    self.submit_callback = submit_callback
    self.task_id = task_id
  
    #* Create PopUp Window to add a new task
    self.form_window = tk.Toplevel(root)  #* Toplevel() is used to create a top-level window, just an independent window that pops up separately from the main application 
    self.form_window.title("Task Form")  #* This is the title of the window
    
    #* Just like label in HTML
    tk.Label(self.form_window, text="Task:").pack() 
    self.task_entry = tk.Entry(self.form_window)
    self.task_entry.pack()  #* Organizes widgets in blocks before placing them in the parent widget
    if task:
      self.task_entry
    
    priority_label = tk.Label(form_window, text="Priority (Low, Medium, High):")
    priority_label.pack()
    self.priority_entry = tk.Entry(form_window)
    self.priority_entry().pack()
    
    due_date_label = tk.Label(form_window, text="Due Date (YYYY-MM-DD):")
    due_date_label.pack()
    self.due_date_entry = tk.Entry(form_window)
    self.due_date_entry.pack()
    
    submit_button = tk.Button(self.form_window, text="Submit", command=self.submit)  #* The command argument: we must pass a function declared to it
    submit_button.pack()
  
  def submit(self):
    task = self.task_entry.get()
    priority = self.priority_entry.get()
    due_date = self.due_date_entry.get()
    
    if self.task_id:
      self.submit_callback(self.task_id, task, priority, due_date)
    else:
      self.submit_callback(task, priority, due_date)
    
    self.form_window.destroy()
    