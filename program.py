def collect_hb_history():
    entry_count = int(input("How many Hb records do you want to enter? "))
    hb_history = {}

    for _ in range(entry_count):
        date = input("Enter date (YYYY-MM-DD): ")
        hb = float(input("Enter Hb value for that date: "))
        hb_history[date] = hb

    return hb_history


def print_hb_chart(hb_history):
    print("\nYour Hb trend:")
    for date, hb in hb_history.items():
        bars = "▓" * int(hb * 2)
        print(f"{date} | {bars:<20} {hb}")

def save_hb_to_csv(hb_history):
    file = open("hb_data.csv", "w")
    file.write("date,hb\n")
    for date, hb in hb_history.items():
        file.write(f"{date},{hb}\n")
    file.close()
    print('\nSaved data.')

def main():
    print("Welcome to Health Tracker!")
    name = input("What is your name? ")

    hb_history = collect_hb_history()
    print(f"\nHi {name},")
    print(hb_history)

    print_hb_chart(hb_history)
    

main()
