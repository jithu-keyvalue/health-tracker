print("Welcome to Vitals Tracker!")

name = input("What is your name? ")
gender = input("What is your gender? (male/female): ")

entry_count = int(input("How many Hb records do you want to enter? "))
hb_history = {}

for i  in range(entry_count):
    date = input("Enter date (YYYY-MM-DD): ")
    hb = float(input("Enter Hb value for that date: "))
    hb_history[name] = hb

print(f"\nHi {name}, here is your Hb history:")
print(hb_history)
