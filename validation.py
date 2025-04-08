import re

def get_name():
    name = ""
    while not name.strip():
        name = input("What is your name? ").strip()
    return name

def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            return date
        print("Invalid date format. Use YYYY-MM-DD.")

def get_hb():
    while True:
        try:
            hb = float(input("Enter Hb value: "))
            if hb > 0:
                return hb
            print("Hb must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
