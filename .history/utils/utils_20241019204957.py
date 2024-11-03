from datetime import datetime

def validate_data(date_text):
  try:
    datetime.strptime(date_text, '%Y-%m-%d')   #* strptime: stands for 
    return True
  except ValueError:
    return False