from datetime import datetime

def validate_data(date_text):
  try:
    input_date = datetime.strptime(date_text, '%Y-%m-%d').date()  #* Input the date part
    if input_date >= datetime.now().date():
      return True
  except ValueError:
    return False