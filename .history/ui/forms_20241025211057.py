import tkinter as tk

class TaskForm:
  def __init__(self, root, add_task_callback):
    self.root = root
    self.add_task_callback = add_task_callback
  
    #* Create PopUp Window to add a new task
    form_window = tk.Toplevel(self.root)  #* Toplevel() is used to create a top-level window, just an independent window that pops up separately from the main application 
    form_window.title("Add New Task")  #* This is the title of the window
    
    task_label = tk.Label(form_window, text="Task:")  #* Just like label in HTML
    task_label.pack()
    self.task_entry = tk.Entry(form_window)
    self.task_entry.pack()  #* Organizes widgets in blocks before placing them in the parent widget
    
    priority_label = tk.Label(form_window, text="Priority (Low, Medium, High):")
    priority_label.pack()
    self.priority_entry = tk.Entry(form_window)
    self.priority_entry().pack()
    
    due_date_label = tk.Label(form_window, text="Due Date (YYYY-MM-DD):")
    due_date_label.pack()
    self.due_date_entry = tk.Entry(form_window)
    self.due_date_entry.pack()
    
    submit_button = tk.Button(form_window, text="Submit", command=self.submit)  #* The command argument: we must pass a function declared to it
    submit_button.pack()
  
  def submit(self):
    task = self.task_entry.get()
    priority = self.priority_entry.get()
    due_date = self.due_date_entry.get()
    
    if self.task_id:
      self.submit_callback(self.task_id, )
    