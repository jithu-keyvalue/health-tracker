def collect_hb_history():
    entry_count = int(input("How many Hb records do you want to enter? "))
    hb_history = {}

    for _ in range(entry_count):
        date = input("Enter date (YYYY-MM-DD): ")
        hb = float(input("Enter Hb value for that date: "))
        hb_history[date] = hb

    return hb_history


def print_hb_chart(hb_history):
    print("\nHemoglobin Chart:\n")
    for date, hb in hb_history.items():
        bars = "▓" * int(hb * 2)
        print(f"{date} | {bars:<20} {hb}")


def main():
    print("Welcome to Health Tracker!")
    name = input("What is your name? ")

    hb_history = collect_hb_history()
    print(f"\nHi {name}, here is your Hb history:")
    print(hb_history)

    print_hb_chart(hb_history)

