from datetime import datetime

def validate_data(date_text):
  try:
    datetime.strptime(date_text, '%Y-%m-%d')
    return True
  except ValueError:
    return False