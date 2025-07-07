print("Welcome to Health Tracker!")

name = input("What is your name? ")
entry_count = int(input("How many Hb records do you want to enter? "))

date_to_hb = {}  # Dictionary: date → hb value

for i in range(entry_count):
    date = input("Enter date (YYYY-MM-DD): ")
    hb = float(input("Enter Hb value for that date: "))
    date_to_hb[name] = hb

print(f"\nHi {name}, here is your Hb history:")
print(date_to_hb)
