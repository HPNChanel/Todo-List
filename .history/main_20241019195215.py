from database.database import connect_db
from ui.ui import create_ui

def main():
  connect_db()
  create_ui()


if __name__ == "__main__":
  main()