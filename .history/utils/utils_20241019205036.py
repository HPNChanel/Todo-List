from datetime import datetime

def validate_data(date_text):
  try:
    datetime.strptime(date_text, '%Y-%m-%d')   #* strptime: stands for string parse time, used to parse a string representing a date and/or time
    return True
  except ValueError:
    return False